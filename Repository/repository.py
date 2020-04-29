from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Repository.read_csv import get_all_weather
from Repository.load_data import load_weather
from urllib import parse


class Repository:
    Base = automap_base()
    Airlines = None
    Planes = None
    Weather= None
    Flights = None
    Engine = None

    def __init__(self, connection_string):
        params = parse.quote_plus(connection_string)
        self.Engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params, fast_executemany=True)
        self.Base.prepare(self.Engine, reflect=True)
        self.Airlines = self.Base.classes.Airlines
        self.Planes = self.Base.classes.Planes
        self.Flights = self.Base.classes.Flights
        self.Weather = self.Base.classes.Weather
        load_weather(get_all_weather(),self.Engine)

    def get_all_airlines(self):
        session = Session(self.Engine)
        all_airlines = session.query(self.Airlines).all()
        session.close()
        return all_airlines

    def get_all_planes(self):
        session = Session(self.Engine)
        all_planes = session.query(self.Planes).all()
        session.close()
        return all_planes

    def get_all_weather(self):
        session = Session(self.Engine)
        all_weather = session.query(self.Weather).all()
        session.close()
        return all_weather

