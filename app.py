import grpc
import time
import logging
import os

from Controller.AirlinesController import add_airlines_controller_to_server
from Controller.PlanesController import add_planes_controller_to_server
from Controller.WeatherController import add_weather_controller_to_server
from Controller.AirportsController import add_airports_controller_to_server
from Controller.FlightsController import add_flights_controller_to_server
from Repository.repository import Repository
from concurrent import futures

DATABASE_USERNAME = os.environ['DATABASE_USERNAME']
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_SERVER = os.environ['DATABASE_SERVER']
DATABASE_PORT = os.environ['DATABASE_PORT']
DATABASE_NAME = os.environ['DATABASE_NAME']


def serve():
    connection_string = 'postgres+psycopg2://{0}:{1}@{2}:{3}/{4}'.format(DATABASE_USERNAME,
                                                                         DATABASE_PASSWORD,
                                                                         DATABASE_SERVER,
                                                                         DATABASE_PORT,
                                                                         DATABASE_NAME)

    # Initialize Repository
    repository = Repository(connection_string)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
        ('grpc.max_send_message_length', -1),
        ('grpc.max_receive_message_length', -1),
    ])

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

    print("Server running on port 80")
    server.add_insecure_port('[::]:80')
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
