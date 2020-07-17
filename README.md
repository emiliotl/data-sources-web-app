# data-sources-web-app
This is a Web Application using Flask with the objective of using different data sources which are a database with PostgreSQL, a dataset from Kaggle using Pandas and an API with gspread to retrieve and update registers from all of them.

## Requirements
- Python 3.X
- PostgreSQL installed and running
- A Gmail account
- A package management system (pip, conda, etc.)

## Installation
First of all, you will need to have all required modules, in my case I use conda, so, to download all of them, once you are (preferably) on your virtual env, run `conda install --yes --file requirements.txt` in your terminal located on the project home directory. 

The project includes the Air Passengers dataset from Kaggle, you can see it on [this page](https://www.kaggle.com/rakannimer/air-passengers). 

Then, for the database, download the dvdrental database from the [PostgreSQL tutorial page](https://sp.postgresqltutorial.com/wp-content/uploads/2019/05/dvdrental.zip) and, once you create a database named "dvdrental" with your user, unzip the downloaded file to get a .tar file and run `pg_restore -c -d dvdrental -v 'path/to/dvdrental.tar' -W` changing the path to the corresponding yours and assuming you have all psql commands in the PATH. Then go to the [dao.py file](https://github.com/emiliotl/data-sources-web-app/blob/master/dao.py) and enter the missing database credentials on psycopg2 connection.

For the Google Spreadsheet, you will need to enable both the Google Drive API and Google Sheets API for your account. Once you enter the basic required information, you will be able to download a JSON file with the credentials, save it in a safe place and add the path to that file (with the file name included) on the empty string from `creds` variable declaration on the [app.py file](https://github.com/emiliotl/data-sources-web-app/blob/master/app.py). Also, you will need to create a spreadsheet with your gmail account, named it `Sample` and add data to the first two columns, naming A1 and B1 as `product` and `count`, respectively, and bellow them, enter any text you want to. Once you finish, share the spreadsheet to the email mentioned on the JSON file.

To run the application, just enter `python3 app.py` on your terminal located on the project home directory and access `localhost:4995` where you can experiment with the endpoints configured, there are some with GET request were you need to put query strings as the code expects to retrieve data, and a form to put data on each data source where you need to pass as query string a keyword to choose from `dataframe`, `database` and `drive`, fill the form and once submitted, the data will be reflected if you use the get endpoints.
