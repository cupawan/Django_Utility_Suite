import os
import json
import gspread
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google.oauth2.service_account import Credentials

class GoogleSheetsAutomation:
    def __init__(self):
        self.secrets_filename = os.environ["GoogleClientSecretPath"]

    def set_up_gc(self):
        gc = gspread.service_account(filename= self.secrets_filename)
        return gc

    def select_worksheet(self,sheet_name = None, worksheet_index = None, sheet_url = None, worksheet_name = None):
        if sheet_url:
            wks = self.set_up_gc().open_by_url(sheet_url)
        elif sheet_name:
            wks = self.set_up_gc().open(sheet_name)
        if worksheet_index == 0 or worksheet_index:
            sh = wks.get_worksheet(worksheet_index)
        elif worksheet_name:
            sh = wks.get_worksheet(worksheet_name)
        return sh

    def insert_values(self,sheet,range_of_cells = None, range_of_cells_vlaues:list = None, single_cell = False, single_cell_value = None,append_row = None, append_rows = None):
        if range_of_cells:
            sheet.update(range_name = range_of_cells, values = [range_of_cells_vlaues])
        elif single_cell:
            sheet.update([[single_cell_value]], single_cell )
        elif append_row:
            sheet.append_row(append_row)
        elif append_rows:
            sheet.append_rows(append_rows)

    def create_new_worksheet(self, new_worksheet_title):
        try:
            self.set_up_gc().create(new_worksheet_title)
            return True
        except Exception as e:
            print(f"Error while creating sheet: {e}")
            return False

    def clear_sheet(self, sh):
        try:
            sh.clear()
            return True
        except Exception as e:
            print(f"Error while clearing sheet: {e}")
            return False

    def format_sheet(self,sh, params:dict, range):
        try:
            sh.format(range, {'textFormat': params})
            return True
        except Exception as e:
            print(f"Error while formatting sheet: {e}")
            return False
    def upload_basic(self, filename,folder_id="1ICryXSfoNB-5S8pdQJ8VYTuwF_M8_tLC"):
        print("Starting file upload process")
        with open(filename, "wb+") as destination:
            for chunk in filename.chunks():
                destination.write(chunk)
        print("Starting Google Drive API Process")
        SERVICE_ACCOUNT_FILE = self.secrets_filename
        SCOPES = ["https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        try:
            service = build("drive", "v3", credentials=creds)
            file_metadata = {"name": filename}
            file_metadata["parents"] = [folder_id]
            media = MediaFileUpload(filename, mimetype="image/jpeg")
            file = (service.files().create(body=file_metadata, media_body=media, fields="id").execute())
            print(f'File ID: {file.get("id")}')
            return file.get("id")
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None