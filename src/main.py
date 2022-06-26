from helpers.extract import get_cot_flip_df
from helpers.plot import plot_cot_flip

if __name__ == '__main__':
    year = 2022
    df = get_cot_flip_df(year)
    plot_cot_flip(df, year)

