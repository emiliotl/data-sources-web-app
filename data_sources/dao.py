from data_sources.database import Database
from data_sources.dataframe import DataFrame
from data_sources.spreadsheet import SpreadSheet


class DataAccessObjectFactory:

    def __init__(self, data_source):
        self.data_source = data_source

    def get_data_access_object(self):
        if self.data_source == 'Database':
            data_access_object = Database(
                {
                    'host': '',
                    'database': '',
                    'user': '',
                    'password': ''
                }
            )
        elif self.data_source == 'DataFrame':
            data_access_object = DataFrame('kaggle_data/AirPassengers.csv')
        else:
            data_access_object = SpreadSheet('')
        return data_access_object.get_source_access_object()
