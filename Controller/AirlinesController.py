import Protos.airlines_pb2_grpc as airlines_pb2_grpc
import Protos.airlines_pb2 as airlines_pb2


def add_airlines_controller_to_server(server, repository):
    airlines_pb2_grpc.add_AirlinesServicer_to_server(AirlinesController(repository), server)


class AirlinesController(airlines_pb2_grpc.AirlinesServicer):
    repository = None

    def __init__(self, repository):
        self.repository = repository

    def GetAirlines(self, request, context):
        all_airlines = self.repository.get_all_airlines()
        grpc_airlines = []
        for data in all_airlines:
            grpc_airlines.append(airlines_pb2.Airline(carrier=data.carrier, name=data.name))
        return airlines_pb2.AirlineResponse(airlines=grpc_airlines)
