import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_cot_flip(df):
    """
    This script plots the Commitment of Traders Reports flip
    for all assets/tickers/contracts in the COT dataframe
    """

    tickers = df['Market_and_Exchange_Names'].unique()
    for ticker in tickers:
        try:
            sub_df = df[df['Market_and_Exchange_Names'] == ticker]
            fig, ax = plt.subplots()
            ax.plot(sub_df['Report_Date_as_MM_DD_YYYY'], sub_df['Flip'], '-x')
            plt.grid()
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
            fig.autofmt_xdate()
            chart_dir = '../data/COT/charts/2020/not_flipped/'
            if any(sub_df['Flip'] > 0) and any(sub_df['Flip'] < 0):
                print(f'Traders have flipped for {ticker}')
                chart_dir = chart_dir.replace('not_flipped', 'flipped')
            fig.savefig(chart_dir + f"{ticker}.png")
            plt.close(fig)
            df.to_csv(f"../data/COT/raw_chart_data/cot_flip_raw_data_for_{ticker}.csv", index=False)
        except Exception as e:
            print(e)
