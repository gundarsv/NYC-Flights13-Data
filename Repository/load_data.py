from sqlalchemy.types import Integer, String, Float
from pandas.api.types import is_string_dtype, is_int64_dtype, is_float_dtype, is_object_dtype


def load_airlines(all_airlines, engine):
    all_airlines.to_sql('airlines',
                        engine,
                        if_exists='append',
                        dtype=create_dtypes(all_airlines),
                        index=False,
                        method='multi',
                        chunksize=50)


def load_planes(all_planes, engine):
    all_planes.to_sql('planes',
                      engine,
                      if_exists='append',
                      dtype=create_dtypes(all_planes),
                      index=False,
                      method='multi',
                      chunksize=50)


def load_weather(all_weather, engine):
    all_weather.to_sql('weather',
                       engine,
                       if_exists='append',
                       dtype=create_dtypes(all_weather),
                       index=False,
                       method='multi',
                       chunksize=50)


def load_airports(all_airports, engine):
    all_airports.to_sql('airports',
                        engine,
                        if_exists='append',
                        dtype=create_dtypes(all_airports),
                        index=False,
                        method='multi',
                        chunksize=50)


def load_flights(all_flights, engine):
    all_flights.to_sql('flights',
                       engine,
                       if_exists='append',
                       dtype=create_dtypes(all_flights),
                       index=False,
                       method='multi',
                       chunksize=50)


def create_dtypes(df):
    dtypes = {}

    for key, value in df.dtypes.items():
        if is_string_dtype(value):
            dtypes.update({'{}'.format(key): String})

        elif is_int64_dtype(value):
            dtypes.update({'{}'.format(key): Integer})

        elif is_float_dtype(value):
            dtypes.update({'{}'.format(key): Float})

        elif is_object_dtype(value):
            dtypes.update({'{}'.format(key): Float})

    return dtypes
