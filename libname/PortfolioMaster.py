
import time
import datetime
import requests
import pandas as pd


class PortfolioMaster():
    """
    PortfolioMaster constructor
    """
    def __init__(self, file_path: str=None, conversion_tokens:list=("USD",)):
        if file_path:
            self.dataframe=self.dataset_from_csv(file_path)
            # This is the list of distinct tokens from dataframe
            self.token_names=self.dataframe.token.unique()

        # This is the list of currencies in which the portfolio balance will be converted and shown
        self.conversion_tokens = conversion_tokens


    """
    dataframe setter function
    """
    def __set_dataset(self, new_dataframe: pd.DataFrame) -> None:
        self.dataframe = new_dataframe
        self.token_names = new_dataframe.token.unique()

    """
    conversion token add function
    """

    def add_conversion_token(self, new_token: str) -> None:
        self.conversion_tokens.append(new_token)

    """
    Get current rates of conversable currencies of a token
    """
    def __get_rates(self,token:str):
        try:
            token_str=",".join(self.conversion_tokens)
            req=requests.get(url="https://min-api.cryptocompare.com/data/price?fsym="+token+"&tsyms="+token_str)
            return req.json()
        except Exception as e:
            print(str(e))
            return 0

    """
    Retrieve dataframe from csv file
    This function retrieve dataframe from csv file using pandas
    """
    def dataset_from_csv(self,file_path) -> pd.DataFrame:
        try:
            # reading csv
            print("Reading file {file_path} ...".format(file_path=file_path))
            s_time = time.time()
            chunks = pd.read_csv(file_path,chunksize=100000)
            dataframe=pd.concat(chunks,ignore_index=True)
            e_time = time.time()
            print("Read with pandas: ", (e_time - s_time), "seconds : rows ", dataframe.shape[0],"\n")
            self.__set_dataset(new_dataframe=dataframe)
            return dataframe
        except Exception as e:
            err = 'Invalid file path'
            print(err)
            pass

    """
    Get portfolio balance for a token
    This function takes token name as parameter and returns portfolio balance for that token in all conversable currencies
    """
    def portfoilo_balance(self, token,date_str:str=None,chunks:int=3) -> float:
        try:
            print("--- Calculating for " + token)
            """
            setting minimum and maximun time range for calculation
            if no date is given then minimun timestamp will be set to 0 and current time as maximum in seconds
            else given date start and ending will be set as range in seconds
            """
            min_timestamp = int(datetime.datetime.strptime(date_str, "%d/%m/%Y").timestamp()) if date_str else 0
            max_timestamp = int(datetime.datetime.strptime(date_str, "%d/%m/%Y").timestamp() + (24 * 60 * 60) - 1) if date_str else time.time()

            # calculating total deposits for token in timestamp range
            total_deposit = self.dataframe.loc[
                    (self.dataframe.timestamp>=min_timestamp) &
                    (self.dataframe.timestamp<=max_timestamp) &
                    (self.dataframe.token == token) &
                    (self.dataframe.transaction_type == "DEPOSIT")
                ][['amount']].sum()['amount']

            # calculating total withdrawals for token in timestamp range
            total_withdrawal = self.dataframe.loc[
                    (self.dataframe.timestamp>=min_timestamp) &
                    (self.dataframe.timestamp<=max_timestamp) &
                    (self.dataframe.token == token) &
                    (self.dataframe.transaction_type == "WITHDRAWAL")
                ][['amount']].sum()['amount']

            # fetching current usd rate for given token
            current_usd_rate= self.__get_rates(token=token)['USD']
            # generating portfolio balance in USD
            usd_portfolio_balance = (total_deposit - total_withdrawal)*current_usd_rate
            print("1 {token} = {rate} USD\nPortfolio balance of {token} : {portfolio_balance} \n".format(token=token,rate=current_usd_rate,portfolio_balance=usd_portfolio_balance))
            return usd_portfolio_balance
        except Exception as e:
            print(str(e))
            pass

    """
    Calculation of portfolio balance at current time for each token type in dataset
    """
    def all_portfoilo_balance(self,date_str:str=None) -> list:
        try:
            print("--- calculating portfolio balance for ",",".join(self.token_names))
            s_time = time.time() # calculation start time log
            result_arr=[]
            for token in self.token_names:
                # calculating portfolio balance for each token in dataset
                result_arr.append({"token":token,"balance":self.portfoilo_balance(token=token,date_str=date_str)})

            e_time = time.time() # calculation end time log
            print("Total exc time: ", (e_time - s_time), "seconds") # printing calculation time duration
            for item in result_arr: print("{token}:{balance}".format(token=item['token'],balance=item['balance']))
            return result_arr
        except Exception as e:
            print(str(e))
            pass


    """
        this static helper method takes the sys argument list as parameter and returns a dict with processed keys and their 
        values
    """
    @staticmethod
    def process_commands(args):
        tags = {}
        # iteration for each 2 items in argument list
        for index in range(1, len(args), 2):
            tags[args[index]] = args[index + 1]
        for tag in tags:print("{tag}:{val}".format(tag=tag,val=tags[tag]))
        return tags


    """
    porfolio balance generation driver function for given requirements
    1. Given no parameters, return the latest portfolio value per token in USD
    2. Given a token, return the latest portfolio value for that token in USD
    3. Given a date, return the portfolio value per token in USD on that date
    4. Given a date and a token, return the portfolio value of that token in USD on that date
    """
    def driver(self,file_path:str,token:str=None,date:str=None):
        try:
            self.dataset_from_csv(file_path=file_path)
            if token and date:
                # Given a date and a token, return the portfolio value of that token in USD on that date
                balance = self.portfoilo_balance(token=token, date_str=date)
            elif token:
                # Given a token, return the latest portfolio value for that token in USD
                balance=self.portfoilo_balance(token=token)
            elif date:
                # Given a date, return the portfolio value per token in USD on that date
                balance_arr = self.all_portfoilo_balance(date_str=date)
            else:
                # Given no parameters, returning the latest portfolio value per token in USD
                balance_arr = self.all_portfoilo_balance()

        except Exception as e:
            print(str(e))
