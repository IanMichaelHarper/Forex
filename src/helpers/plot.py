import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os


def plot_cot_flip(df, year):
    """
    This script plots the Commitment of Traders Reports flip
    for all assets/tickers/contracts in the COT dataframe
    """

    tickers = df['Market_and_Exchange_Names'].unique()
    for ticker in tickers:
        ticker = ticker.replace("/", "-")
        sub_df = df[df['Market_and_Exchange_Names'] == ticker]
        fig, ax = plt.subplots()
        ax.plot(sub_df['Report_Date_as_MM_DD_YYYY'], sub_df['Flip'], '-x')
        plt.grid()
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%y'))
        fig.autofmt_xdate()
        chart_dir = f'../data/COT/charts/{year}/not_flipped/'
        if any(sub_df['Flip'] > 0) and any(sub_df['Flip'] < 0):
            print(f'Traders have flipped for {ticker}')
            chart_dir = chart_dir.replace('not_flipped', 'flipped')
            ax.plot(sub_df['Report_Date_as_MM_DD_YYYY'], [0 for i in sub_df['Flip']])
        plt.suptitle(ticker)
        plt.title("above 0: net long, below 0: net short")
        plt.xlabel(f"Date")
        plt.ylabel("Hedge fund positioning")
        fig.savefig(chart_dir + f"{ticker}.png")
        plt.close(fig)
        df.to_csv(os.path.join(chart_dir, f"cot_flip_raw_data_for_{ticker}.csv"), index=False)
