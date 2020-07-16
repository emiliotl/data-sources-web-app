from flask import Flask
from pandas import read_csv

app = Flask(__name__)


@app.route('/')
def home_page():
    return "Welcome"


@app.route('/get_pandas_data', methods=['GET'])
def get_pandas_data():
    air_passengers_data_frame = read_csv('kaggle_data/AirPassengers.csv')
    return {air_passengers_data_frame['time'][0]: str(air_passengers_data_frame['value'][0])}


app.run(port=4995)
