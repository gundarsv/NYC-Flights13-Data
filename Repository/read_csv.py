import pandas as pd

AIRLINES_CSV_PATH = 'D:/ViaUC/SEP6 - NYC Flights 13 - Documents/Data/airlines.csv'
PLANES_CSV_PATH = 'D:/ViaUC/SEP6 - NYC Flights 13 - Documents/Data/planes.csv'
WEATHER_CSV_PATH = 'D:/ViaUC/SEP6 - NYC Flights 13 - Documents/Data/weather.csv'
AIRPORTS_CSV_PATH = 'D:/ViaUC/SEP6 - NYC Flights 13 - Documents/Data/airports.csv'
FLIGHTS_CSV_PATH = 'D:/ViaUC/SEP6 - NYC Flights 13 - Documents/Data/flights.csv'


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
                                 'year': pd.Int64Dtype(),
                                 'month': pd.Int64Dtype(),
                                 'day': pd.Int64Dtype(),
                                 'hour': pd.Int64Dtype(),
                                 'temp': 'float64',
                                 'dewp': 'float64',
                                 'humid': 'float64',
                                 'wind_dir': pd.Int64Dtype(),
                                 'wind_speed': 'float64',
                                 'wind_gust': 'float64',
                                 'precip': 'float64',
                                 'pressure': 'float64',
                                 'visib': 'float64',
                                 'time_hour': pd.StringDtype(),
                                 })
    df = replace_nan_with_none(weather)
    return df


def get_all_airports():
    airports = pd.read_csv(AIRPORTS_CSV_PATH,
                           dtype={'faa': pd.StringDtype(),
                                  'name': pd.StringDtype(),
                                  'lat': 'float64',
                                  'lon': 'float64',
                                  'alt': pd.Int64Dtype(),
                                  'tz': pd.Int64Dtype(),
                                  'dst': pd.StringDtype(),
                                  'tzone': pd.StringDtype()})
    df = replace_nan_with_none(airports)
    return df


def get_all_flights():
    flights = pd.read_csv(FLIGHTS_CSV_PATH,
                          dtype={'origin': pd.StringDtype(),
                                 'dest': pd.StringDtype(),
                                 'carrier': pd.StringDtype(),
                                 'tailnum': pd.StringDtype(),
                                 'flight': pd.Int64Dtype(),
                                 'year': pd.Int64Dtype(),
                                 'month': pd.Int64Dtype(),
                                 'day': pd.Int64Dtype(),
                                 'dep_time': pd.Int64Dtype(),
                                 'dep_delay': pd.Int64Dtype(),
                                 'arr_time': pd.Int64Dtype(),
                                 'arr_delay': pd.Int64Dtype(),
                                 'air_time': pd.Int64Dtype(),
                                 'distance': pd.Int64Dtype(),
                                 'hour': pd.Int64Dtype(),
                                 'minute': pd.Int64Dtype()})
    df = replace_nan_with_none(flights)
    return df


def replace_nan_with_none(df):
    return df.where(pd.notnull(df), None)
