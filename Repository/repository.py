from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class Repository:
    Base = automap_base()
    Airlines = None
    Planes = None
    Weather = None
    Flights = None
    Engine = None

    def __init__(self, connection_string):
        self.Engine = create_engine(connection_string)
        self.Base.prepare(self.Engine, reflect=True)
        self.Airlines = self.Base.classes.airlines
        self.Planes = self.Base.classes.planes
        self.Flights = self.Base.classes.flights
        self.Weather = self.Base.classes.weather

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

    def get_engine(self):
        return self.Engine
