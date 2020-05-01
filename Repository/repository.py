from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session


class Repository:
    Base = automap_base()
    Airlines = None
    Planes = None
    Weather = None
    Flights = None
    Airports = None
    Engine = None

    def __init__(self, connection_string):
        self.Engine = create_engine(connection_string)
        self.Base.prepare(self.Engine, reflect=True)
        self.Airlines = self.Base.classes.airlines
        self.Planes = self.Base.classes.planes
        self.Flights = self.Base.classes.flights
        self.Weather = self.Base.classes.weather
        self.Airports = self.Base.classes.airports

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

    def get_all_airports(self):
        session = Session(self.Engine)
        all_airports = session.query(self.Airports).all()
        session.close()
        return all_airports

    def get_all_flights(self):
        session = Session(self.Engine)
        all_flights = session.query(self.Flights).all()
        session.close()
        return all_flights

    def get_number_of_flights_per_month(self, month_number):
        session = Session(self.Engine)
        number_of_flights = session.query(func.count(self.Flights.day)).filter(self.Flights.month == month_number).scalar()
        session.close()
        return number_of_flights

    def get_engine(self):
        return self.Engine
