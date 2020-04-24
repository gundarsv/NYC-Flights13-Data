import grpc

# import the generated classes
import Protos.greet_pb2_grpc as greet_pb2_grpc
import Protos.greet_pb2 as greet_pb2

# read in certificate
with open('server.crt', 'rb') as f:
    trusted_certs = f.read()

# create credentials
credentials = grpc.ssl_channel_credentials(root_certificates=trusted_certs)

# open a gRPC channel
channel = grpc.secure_channel('localhost:5001', credentials)

# create a stub (client)
stub = greet_pb2_grpc.GreeterStub(channel)

# create a valid request message
hello_request = greet_pb2.HelloRequest(name="gundars")

# make the call
response = stub.SayHello(hello_request)

# print response message
print(response.message)