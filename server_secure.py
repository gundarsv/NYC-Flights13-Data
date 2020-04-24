import grpc
import time
import logging

from concurrent import futures

import Protos.greet_pb2_grpc as greet_pb2_grpc
import Protos.greet_pb2 as greet_pb2


with open('D:\Cert\server.key', 'rb') as f:
    private_key = f.read()
with open('D:\Cert\server.crt', 'rb') as f:
    certificate_chain = f.read()


class Greeter(greet_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return greet_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server_credentials = grpc.ssl_server_credentials(
        ((private_key, certificate_chain,),))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greet_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_secure_port('[::]:5001', server_credentials)
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    logging.basicConfig()
    serve()
