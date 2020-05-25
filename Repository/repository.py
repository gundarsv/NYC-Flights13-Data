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
        self.Planes = self.Base.classes.planes
        self.Flights = self.Base.classes.flights
        self.Weather = self.Base.classes.weather
        self.Airports = self.Base.classes.airports
        self.Airlines = self.Base.classes.airlines

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
        number_of_flights = session.query(func.count('*').label('count'), self.Flights.month.label('month'))\
            .filter(self.Flights.month == month_number)\
            .group_by(self.Flights.month).one()

        session.close()
        return number_of_flights

    def get_number_of_flights_in_months(self, month_numbers):
        session = Session(self.Engine)
        number_of_flights = session.query(func.count('*').label('count'), self.Flights.month.label('month'))\
            .filter(self.Flights.month.in_(month_numbers))\
            .group_by(self.Flights.month).all()

        session.close()
        return number_of_flights

    def get_manufacturers_with_more_than_200_planes(self):
        session = Session(self.Engine)
        manufacturers_with_more_than_200_planes = session.query(func.count('*').label('planesTotal'), self.Planes.manufacturer.label('manufacturer'))\
            .having(func.count('*') >= 200)\
            .group_by(self.Planes.manufacturer).all()

        session.close()
        return manufacturers_with_more_than_200_planes;

    def get_temperature_at_origin(self, origin):
        session = Session(self.Engine)
        temperatures_at_origin = session.query(self.Weather.year, self.Weather.month, self.Weather.day, self.Weather.hour, self.Weather.temp, self.Weather.origin)\
            .filter(self.Weather.origin == origin)\
            .all()

        session.close()
        return temperatures_at_origin

    def get_top_10_destinations_for_origin(self, origin):
        session = Session(self.Engine)
        top_10_destinations_for_origin = session.query(func.count('*').label('numberOfFlights'), self.Flights.dest.label('destination'), self.Flights.origin)\
            .filter(self.Flights.origin == origin)\
            .group_by(self.Flights.dest, self.Flights.origin)\
            .order_by(func.count('*').desc())\
            .limit(10)\
            .all()

        session.close()
        return top_10_destinations_for_origin

    def get_airtime_at_origin(self, origin):
        session = Session(self.Engine)
        airtime_at_origin = session.query(self.Flights.air_time)\
            .filter(self.Flights.origin == origin)\
            .all()

        session.close()
        return airtime_at_origin;

    def get_mean_airtime_at_origins(self, origins):
        session = Session(self.Engine)
        airtime_at_origins = session.query(self.Flights.air_time,self.Flights.origin) \
            .filter(self.Flights.origin.in_(origins))\
            .group_by(self.Flights.origin,self.Flights.air_time)\
            .all()

        session.close()
        return airtime_at_origins

    def get_weather_observations_at_origin(self, origin):
        session = Session(self.Engine)
        observations_at_origin = session.query(func.count('*').label('observationsAtOrigin'), self.Weather.origin) \
            .filter(self.Weather.origin == origin) \
            .group_by(self.Weather.origin)\
            .one()

        session.close()
        return observations_at_origin

    def get_weather_observations_at_origins(self, origins):
        session = Session(self.Engine)
        observations_at_origins = session.query(func.count('*').label('observationsAtOrigin'), self.Weather.origin) \
            .filter(self.Weather.origin.in_(origins)) \
            .group_by(self.Weather.origin) \
            .all()

        session.close()
        return observations_at_origins

    def get_temperature_at_origins(self, origins):
        session = Session(self.Engine)
        temperatures_at_origins = session.query(self.Weather.year, self.Weather.month, self.Weather.day, self.Weather.hour, self.Weather.temp, self.Weather.origin)\
            .filter(self.Weather.origin.in_(origins))\
            .group_by(self.Weather.origin, self.Weather.temp, self.Weather.day, self.Weather.month, self.Weather.year,self.Weather.hour, self.Weather.origin)\
            .order_by(self.Weather.year, self.Weather.month, self.Weather.day, self.Weather.hour)\
            .all()

        session.close()
        return temperatures_at_origins

    def get_number_of_flights_per_month_at_origin(self, month_number, origin):
        session = Session(self.Engine)
        number_of_flights_at_origin = session.query(func.count('*').label('count'), self.Flights.month.label('month'), self.Flights.origin)\
            .filter(self.Flights.month == month_number, self.Flights.origin == origin)\
            .group_by(self.Flights.month, self.Flights.origin).one()

        session.close()
        return number_of_flights_at_origin

    def get_number_of_flights_per_month_per_origins(self, month_number, origins):
        session = Session(self.Engine)
        number_of_flights_per_origins = session.query(func.count('*').label('count'), self.Flights.month.label('month'), self.Flights.origin)\
            .filter(self.Flights.month == month_number, self.Flights.origin.in_(origins))\
            .group_by(self.Flights.month, self.Flights.origin) \
            .order_by(self.Flights.month) \
            .all()

        session.close()
        return number_of_flights_per_origins

    def get_number_of_flights_in_months_at_origin(self, month_numbers, origin):
        session = Session(self.Engine)
        number_of_flights_at_origin = session.query(func.count('*').label('count'), self.Flights.month.label('month'), self.Flights.origin) \
            .filter(self.Flights.month.in_(month_numbers)) \
            .filter(self.Flights.origin == origin) \
            .group_by(self.Flights.month, self.Flights.origin) \
            .order_by(self.Flights.month) \
            .all()

        session.close()
        return number_of_flights_at_origin

    def get_number_of_flights_in_months_per_origins(self, month_numbers, origins):
        session = Session(self.Engine)
        number_of_flights_per_origins = session.query(func.count('*').label('count'), self.Flights.month.label('month'), self.Flights.origin) \
            .filter(self.Flights.month.in_(month_numbers)) \
            .filter(self.Flights.origin.in_(origins)) \
            .group_by(self.Flights.month, self.Flights.origin) \
            .order_by(self.Flights.month) \
            .all()

        session.close()
        return number_of_flights_per_origins

    def get_engine(self):
        return self.Engine
