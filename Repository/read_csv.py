import pandas as pd
import numpy as mp


AIRLINES_CSV_PATH = 'D:/ViaUC/SEP6 - NYC Flights 13 - Documents/Data/airlines.csv'
PLANES_CSV_PATH = 'D:/sep6backend/planes.csv'
WEATHER_CSV_PATH= 'D:/sep6backend/weather.csv'


def get_all_airlines():
    airlines = pd.read_csv(AIRLINES_CSV_PATH, dtype={'carrier': pd.StringDtype(),
                                                     'name': pd.StringDtype()})
    df = replace_nan_with_none(airlines)
    return df


def get_all_planes():
    planes = pd.read_csv(PLANES_CSV_PATH,
                         dtype={'tailnum': pd.StringDtype(),
                                'year': pd.Int64Dtype(),
                                'type': pd.StringDtype(),
                                'manufacturer': pd.StringDtype(),
                                'model': pd.StringDtype(),
                                'engines': pd.Int64Dtype(),
                                'seats': pd.Int64Dtype(),
                                'speed': pd.Int64Dtype(),
                                'engine': pd.StringDtype(),
                                })
    df = replace_nan_with_none(planes)
    return df


def get_all_weather():
    weather = pd.read_csv(WEATHER_CSV_PATH,
                           dtype={'origin': pd.StringDtype(),
                                  'year' : pd.Int64Dtype(),
                                  'month' : pd.Int64Dtype(),
                                  'day' : pd.Int64Dtype(),
                                  'hour' : pd.Int64Dtype(),
                                  'wind_dir' : pd.Int64Dtype(),
                                  'time_hour' : pd.StringDtype(),
                                  })
    df = replace_nan_with_none(weather)
    return df




def replace_nan_with_none(df):
    return df.where(pd.notnull(df), None)
