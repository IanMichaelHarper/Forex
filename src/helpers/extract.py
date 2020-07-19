from __future__ import print_function
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import quandl as q
import pandas as pd


class GSheets(object):
    """
    Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    def __init__(self):
        # If modifying these scopes, delete the file token.pickle.
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

        # The ID and range of a sample spreadsheet.
        self.SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
        self.SAMPLE_RANGE_NAME = 'Class Data!A2:E'

    def get_creds(self):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        return creds

    def get_values(self):
        creds = self.get_creds()
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                    range=self.SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        return values


def get_cot_columns():
    os.system("wget -P ../../data/COT/raw_report/ https://www.cftc.gov/files/dea/history/dea_fut_xls_2020.zip")
    os.system("cd ../data/COT/raw_report/ && unzip dea_com_xls_2020.zip")
    df = pd.read_excel("/home/harperi/Dev/PycharmProjects/Forex/data/COT/raw_report/dea_fut_xls_2020/annual.xls")
    df = df[['Market_and_Exchange_Names', 'Report_Date_as_MM_DD_YYYY', 'NonComm_Positions_Long_All',
             'NonComm_Positions_Short_All', 'Change_in_NonComm_Long_All', 'Change_in_NonComm_Short_All',
             'Pct_of_OI_NonComm_Long_All', 'Pct_of_OI_NonComm_Short_All']]
    df.to_excel("~/Downloads/AUD_COT_2019.xls")


def get_cot_flip_df():
    os.system("wget -P ../data/COT/raw_report/ https://www.cftc.gov/files/dea/history/dea_fut_xls_2020.zip")
    os.system("unzip ../data/COT/raw_report/dea_fut_xls_2020.zip -d ../data/COT/raw_report/")
    df = pd.read_excel("/home/harperi/Dev/PycharmProjects/Forex/data/COT/raw_report/annual.xls")
    df = df[['Market_and_Exchange_Names', 'Report_Date_as_MM_DD_YYYY', 'NonComm_Positions_Long_All',
             'NonComm_Positions_Short_All', 'Change_in_NonComm_Long_All', 'Change_in_NonComm_Short_All',
             'Pct_of_OI_NonComm_Long_All', 'Pct_of_OI_NonComm_Short_All']]
    df['Flip'] = df['Pct_of_OI_NonComm_Long_All'] - df['Pct_of_OI_NonComm_Short_All']

    return df


def get_and_save_quandl_data():
    codes = ["ISM/MAN_PMI",
            "ISM/NONMAN_NMI"
    #        "UMICH/SOC1",
            # no free BP, but quandl has this data for 200+ countries. Think I need an account
    #        "FED/M2_M",  # quandl has data here for other countries
    #        "FED/RIFSPFF_N_M",  # monthly fed funds, quandl has daily rates too (more up to date). Also FRED code of DFF
    #        "FRED/CPIAUCSL",
    #        "FRED/CPIAUCSL",
    #         "FRED/WPSFD49207",  # PPI finished goods
    #        "FRED/WPSFD4131",  # PPI finished goods less foods and energy
    #        "FRED/PAYEMS",  # Non Farm Payrolls NFP
    #        "FRED/FYGDP", # GDP
    #        "FRED/GFDEBTN", #  Total Public Debt
    #        "FRED/GFDEGDQ188S", # Debt to GDP
    #        "FRED/FYFSGDA188S", # Surplus deficit as a % of GDP
    #        "FRED/FYOINT", #  Outlays: Interest (interest bill)
    #        "FRED/FYONET", #  Outlays: Net
    #        "FRED/FYFR", #  Receipts
    #        "FRED/WGS10YR", # 10-year Treasury Bond interest rate
    #        "FRED/WALCL", # Fed Balance Sheet
    #        "FRED/A191RL1Q225SBEA" # Real GDP % Growth
    ]

    for code in codes:
        data = q.get(code)
        data.to_csv(code.split('/')[1] + ".csv", index=False)
