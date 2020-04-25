"""
This script plots the Commitment of Traders Reports flip for all assets/tickers/contracts in the excel file
"""

import pandas as pd
import matplotlib.pyplot as plt

def get_cot_columns():
    df = pd.read_excel("~/Downloads/dea_fut_xls_2019/annual.xls")
    df = df[['Market_and_Exchange_Names', 'Report_Date_as_MM_DD_YYYY',	'NonComm_Positions_Long_All',
             'NonComm_Positions_Short_All',	'Change_in_NonComm_Long_All',	'Change_in_NonComm_Short_All',
             'Pct_of_OI_NonComm_Long_All','Pct_of_OI_NonComm_Short_All']]
    df.to_excel("~/Downloads/AUD_COT_2019.xls")
    exit(1)

df = pd.read_excel("~/Downloads/annual.xls")
df = df[['Market_and_Exchange_Names', 'Report_Date_as_MM_DD_YYYY',	'NonComm_Positions_Long_All',
         'NonComm_Positions_Short_All',	'Change_in_NonComm_Long_All',	'Change_in_NonComm_Short_All',
         'Pct_of_OI_NonComm_Long_All','Pct_of_OI_NonComm_Short_All']]
df['Flip'] = df['Pct_of_OI_NonComm_Long_All'] - df['Pct_of_OI_NonComm_Short_All']
tickers = df['Market_and_Exchange_Names'].unique()
chart_dir = 'data/cot_charts'
for ticker in tickers:
    try:
        sub_df = df[df['Market_and_Exchange_Names'] == ticker]
        plt.figure()
        plt.plot(sub_df['Report_Date_as_MM_DD_YYYY'], sub_df['Flip'])
        plt.savefig(f"cot_charts/{ticker}.png")
        df.to_csv(f"cot_chart_raw_data/cot_flip_raw_data_for_{ticker}.csv", index=False)
    except Exception as e:
        print(e)
