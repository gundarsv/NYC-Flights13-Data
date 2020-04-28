import os
import grpc
import time
import logging

from Controller.AirlinesController import add_airlines_controller_to_server
from Controller.PlanesController import add_planes_controller_to_server
from Repository.repository import Repository
from concurrent import futures

DATABASE_CONNECTION_STRING = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:nycflights13.database.windows.net,1433;Database=nycflights13;Uid=nycflights;Pwd=flights13!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

with open(os.environ['PRIVATE_KEY_PATH'], 'rb') as f:
    private_key = f.read()
with open(os.environ['CERTIFICATE_PATH'], 'rb') as f:
    certificate_chain = f.read()


def serve():
    # Initialize Repository
    repository = Repository(DATABASE_CONNECTION_STRING)

    server_credentials = grpc.ssl_server_credentials(
        ((private_key, certificate_chain),),)

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add AirlinesController To server
    add_airlines_controller_to_server(server, repository)
    add_planes_controller_to_server(server, repository)


    server.add_secure_port('[::]:6001', server_credentials)
    server.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
