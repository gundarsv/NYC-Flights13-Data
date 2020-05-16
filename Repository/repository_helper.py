import pandas as pd


def get_daily_mean_temperature(temperature):
    return pd.DataFrame(temperature).groupby(['year', 'month', 'day'])['temp'].mean().reset_index(name='mean_temperature')
