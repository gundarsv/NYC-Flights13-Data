import pandas as pd


def get_daily_mean_temperature(temperature):
    return pd.DataFrame(temperature).groupby(['year', 'month', 'day', 'origin'])['temp'].mean().reset_index(
        name='mean_temperature')


def get_mean_airtime(airtimes):
    return pd.DataFrame(airtimes).groupby(['origin'])['air_time'].mean().reset_index(name='mean_airtime')


def get_flights_per_manufacturer(flights_with_tailnum_and_manufacturer):
    return pd.DataFrame(flights_with_tailnum_and_manufacturer).groupby(['manufacturer'])['count'].sum().reset_index(
        name='numberOfFlights')


def get_mean_departure_arrival_delay(departure_arrival_delay):
    df = pd.DataFrame(departure_arrival_delay)
    df = df.groupby('origin')[['arr_delay','dep_delay']].mean().reset_index()
    return df
