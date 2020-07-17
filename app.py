from flask import Flask, request
from pandas import read_csv
from oauth2client.service_account import ServiceAccountCredentials
import gspread

import dao

app = Flask(__name__)
data_frame = read_csv('kaggle_data/AirPassengers.csv')
creds = ServiceAccountCredentials.from_json_keyfile_name(
    '',
    ['https://spreadsheets.google.com/feeds',
     'https://www.googleapis.com/auth/drive']
)
sheet = gspread.authorize(creds).open("Sample").sheet1


@app.route('/')
def home_page():
    return "Welcome"


@app.route('/get_pandas_data', methods=['GET'])
def get_pandas_data():
    return {
        index: value for (index, value) in
        data_frame[request.args['column']][:int(request.args['rows'])].items()
    }


@app.route('/get_database_data', methods=['GET'])
def get_database_data():
    return {
        index: value for (index, value) in
        enumerate(dao.query_to_select_data(
            f'select {request.args["column"]} '
            f'from actor limit {request.args["rows"]}'))
    }


@app.route('/get_drive_data', methods=['GET'])
def get_drive_data():
    if request.args:
        return {
            index: value for (index, value) in
            enumerate(sheet.col_values(request.args["column_number"]))
        }
    else:
        return {
            index: value for (index, value) in
            enumerate(sheet.get_all_records())
        }


app.run(port=4995)
