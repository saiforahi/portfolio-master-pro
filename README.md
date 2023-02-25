<a name="readme-top"></a>

<div align="center" >
  <!-- img src="murple_logo.png" alt="logo" width="140"  height="auto" /> 
  <br/-->
  <h1><b>PortfolioMaster</b></h1>
  <h5>Propine Blockchain Engineer Technical Assessment</h5>
</div>

<!-- TABLE OF CONTENTS -->

# 📗 Table of Contents

- [📖 About the Project](#about-project)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Prerequisites](#install-libraries)
  - [Run](#run)
  - [Run tests](#run-tests)
- [⚙️ Methods](#methods)
- [👥 Authors](#authors)
- [🤝 Contributing](#contributing)
- [🙏 Acknowledgements](#acknowledgements)


<!-- PROJECT DESCRIPTION -->

# 📖 PortfolioMaster <a name="about-project"></a>

**portfoliomaster** is a portfolio balance generation program.
To build this program I chose **python** as programming language and used **pandas** data manipulation library to read dataset from csv files 
and manipulate them.<br/>

Since pandas use Contiguous Memory Allocation (consecutive blocks are assigned) and can be presented as array, it is faster in execution also easier to control for OS than other non-contiguous approaches.
In this case, Python is a better choice. PortfolioMaster constructor loads the dataset from csv file in chunks for once in execution cycle.

PortfolioMaster is a class which is designed to perform portfolio balance generations in multiple currency type such as USD, EUR, JPY (currently USD only but extendable). 

It has 3 instance variables 

- `dataframe`
- `token_names`
- `conversion_tokens`

and 4 interactive functionalities

- `current portfolio balance for a specific token`
- `current portfolio balance for each token`
- `portfolio balance for a specific token on a specific date`
- `portfolio balance for each token on a specific date`

besides some common setter-getter functions and a function for token rate retrieving. Details are written in <a href="#methods">**Methods**</a> section.



<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

> steps

To get a local copy up and running, follow these steps.

### Setup

Clone this repository to your desired folder:


Example commands:

```sh
  cd my-folder
  git clone https://github.com/saiforahi/portfolio-master-pro.git
```


project_root/<br/>
│<br/>
├── libname/ #class file <br/>
├── main.py #driver file <br/>
├── README <br/>



### Install libraries:

```sh
 pip install requirements.txt
```

### Run
Command line arguments:

>file tag <br/>
Provide the file path (local/remote) using command line interface with tag `-f`<br/>

>token tag <br/>
Provide the token using command line interface with tag `-t`<br/>

>date tag <br/>
Provide the date using command line interface with tag (d/m/Y) `-d`<br/>

To run the project, execute the following command:


Example command:

```sh
  python main.py -f https://s3-ap-southeast-1.amazonaws.com/static.propine.com/transactions.csv.zip -t BTC -d 02/08/2019
```


### Using as module
To use as module you will have to import the class and initiate an object then call the function with appropriate values.

Example:

>from PortfolioMaster import PortfolioMaster

>pf_master = PortfolioMaster(file_path="data/transactions.csv")

>pf_master.portfolio_balance(token="ETH") # returns latest ETH portfolio balance in USD

>pf_master.all_portfolio_balance(date_str="02/02/2019") # returns all distinct token types' portfolio balance on 2nd Feb, 2019

>pf_master.portfolio_balance(token="BTC",date_str="02/02/2019") # returns BTC portfolio balance in USD for 2nd Feb, 2019

>pf_master.all_portfolio_balance() # returns all distinct token types' latest portfolio balance from dataset




### Run tests

To run tests, run the following command:


Example command:

```sh
  python main.py -f https://s3-ap-southeast-1.amazonaws.com/static.propine.com/transactions.csv.zip -t BTC -d 02/08/2019
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CLASS DESCRIPTION -->

## ⚙️ Methods <a name="methods"></a>

> PortfolioMaster class methods

1️⃣ **dataset_from_csv(file_path)**<br/>
This method is responsible for reading csv file and setting the dataframe.<br/>
<sub>Parameters : </sub><br/>
- `file_path : string`



2️⃣ **portfoilo_balance(token, date_str)** <br/>
This method is responsible for generating portfolio balance for given token on given date.<br/>
<sub>Parameters : </sub><br/>
- `token : string`
- `date_str: string (d/m/Y)`


3️⃣ **all_portfoilo_balance(date_str)** <br/>
This method is responsible for generating portfolio balance for all token types present in dataset on given date (default latest).<br/>
<sub>Parameters : </sub><br/>
- `date_str: string (d/m/Y)`


4️⃣ **driver(tags)** <br/>
This method is responsible for running the test program. This function takes processed tags from command line as dictionary<br/>
<sub>Parameters : </sub><br/>
- `file_path: string`
- `token : string`
- `date_str : string (d/m/Y)`



<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

> Mention all of the collaborators of this project.

👤 **Dev**

- GitHub: [@githubhandle](https://github.com/saiforahi)
- LinkedIn: [LinkedIn](https://linkedin.com/in/shaif-azad-rahi/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](../../issues/).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGEMENTS -->

## 🙏 Acknowledgments <a name="acknowledgements"></a>


I would like to thank **Propine Technical Assessment** team <a href="https://github.com/BenPropine">Ben</a> & <a href="https://github.com/liangzan">Zan</a>
for supporting me understanding the requirements.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

