import grpc

# import the generated classes
import Protos.greet_pb2_grpc as greet_pb2_grpc
import Protos.greet_pb2 as greet_pb2

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = greet_pb2_grpc.GreeterStub(channel)

# create a valid request message
hello_request = greet_pb2.HelloRequest(name="gundars")

# make the call
response = stub.SayHello(hello_request)

# print response message
print(response.message)