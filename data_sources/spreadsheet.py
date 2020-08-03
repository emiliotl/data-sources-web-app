from oauth2client.service_account import ServiceAccountCredentials
import gspread


class SpreadSheet:

    def __init__(self, json_key_file_path):
        self.drive_credential = (
            ServiceAccountCredentials.from_json_keyfile_name(
                json_key_file_path,
                ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
            ))

    def get_source_access_object(self):
        return gspread.authorize(self.drive_credential).open('Sample').sheet1
