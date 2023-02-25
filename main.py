import sys
from libname.PortfolioMaster import PortfolioMaster

if __name__ == '__main__':
    try:
        """ processing commands by looking for -f -t and -d tags for file path, token and date argument values and return
        them as dict """
        tags = PortfolioMaster.process_commands(sys.argv)
        # initiating PortfoiloMatser instance
        portfolio_master = PortfolioMaster()
        # running driver function
        remote_test_csv_file_path="https://s3-ap-southeast-1.amazonaws.com/static.propine.com/transactions.csv.zip"
        portfolio_master.driver(file_path=tags.get("-f",remote_test_csv_file_path), token=tags.get("-t",None),date=tags.get("-d",None))
    except Exception as e:
        print(str(e))

