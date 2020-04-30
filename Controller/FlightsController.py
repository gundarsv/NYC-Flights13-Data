import Protos.flights_pb2_grpc as flights_pb2_grpc
import Protos.flights_pb2 as flights_pb2


def add_flights_controller_to_server(server, repository):
    flights_pb2_grpc.add_FlightsServicer_to_server(FlightsController(repository), server)


class FlightsController(flights_pb2_grpc.FlightsServicer):
    repository = None

    def __init__(self, repository):
        self.repository = repository

    def GetFlights(self, request, context):
        all_flights = self.repository.get_all_flights()
        grpc_flights = []
        for data in all_flights:
            grpc_flights.append(flights_pb2.Flight(origin=data.origin, dest=data.dest, carrier=data.carrier, tailnum=data.tailnum, flight=data.flight, year=data.year, month=data.month, day=data.day, dep_time=data.dep_time, dep_delay=data.dep_delay, arr_time=data.arr_time, arr_delay=data.arr_delay, air_time=data.air_time, distance=data.distance, hour=data.hour, minute=data.minute))
        return flights_pb2.FlightResponse(flight=grpc_flights)

    def GetNumberOfFlightsPerMonth(self, request, context):
        number_of_flights = self.repository.get_number_of_flights_per_month(request.number)
        return flights_pb2.FlightsCount(count=number_of_flights)
