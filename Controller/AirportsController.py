import Protos.airports_pb2_grpc as airports_pb2_grpc
import Protos.airports_pb2 as airports_pb2


def add_airports_controller_to_server(server, repository):
    airports_pb2_grpc.add_AirportsServicer_to_server(AirportsController(repository), server)


class AirportsController(airports_pb2_grpc.AirportsServicer):
    repository = None

    def __init__(self, repository):
        self.repository = repository

    def GetAirports(self, request, context):
        all_airports = self.repository.get_all_airports()
        grpc_airports = []
        for data in all_airports:
            grpc_airports.append(airports_pb2.Airport(faa=data.faa, name=data.name, lat=data.lat, lon=data.lon, alt=data.alt, tz=data.tz, dst=data.dst, tzone=data.tzone))
        return airports_pb2.AirportResponse(airport=grpc_airports)
