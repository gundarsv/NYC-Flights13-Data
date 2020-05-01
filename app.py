import grpc
import time
import logging

from grpc._cython import cygrpc

from Controller.AirlinesController import add_airlines_controller_to_server
from Controller.PlanesController import add_planes_controller_to_server
from Controller.WeatherController import add_weather_controller_to_server
from Controller.AirportsController import add_airports_controller_to_server
from Controller.FlightsController import add_flights_controller_to_server
from Repository.load_data import load_weather, load_airlines, load_planes, load_airports, load_flights
from Repository.read_csv import get_all_weather, get_all_airlines, get_all_planes, get_all_airports, get_all_flights
from Repository.repository import Repository
from concurrent import futures

DATABASE_CONNECTION_STRING = 'postgres+psycopg2://nycflightsadmin@nycflights-postgresql:flights13!@nycflights-postgresql.postgres.database.azure.com:5432/nycflights'


def serve():
    # Initialize Repository
    repository = Repository(DATABASE_CONNECTION_STRING)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_send_message_length', -1),
        ('grpc.max_receive_message_length', -1),
    ])

    # Add AirlinesController To server
    add_airlines_controller_to_server(server, repository)
    add_planes_controller_to_server(server, repository)
    add_weather_controller_to_server(server,  repository)
    add_airports_controller_to_server(server, repository)
    add_flights_controller_to_server(server, repository)

    # engine = repository.get_engine()

    # load_planes(get_all_planes(), engine)
    # load_airlines(get_all_airlines(), engine)
    # load_airports(get_all_airports(), engine)
    # load_weather(get_all_weather(), engine)
    # load_flights(get_all_flights(), engine)

    server.add_insecure_port('[::]:8080')
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
