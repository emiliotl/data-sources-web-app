from pandas import read_csv


class DataFrame:

    def __init__(self, path):
        self.data_frame = read_csv(path)

    def get_source_access_object(self):
        return self.data_frame
