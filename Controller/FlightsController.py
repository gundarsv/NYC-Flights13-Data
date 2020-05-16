import Protos.flights_pb2_grpc as flights_pb2_grpc
import Protos.flights_pb2 as flights_pb2
import numpy as np


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
        return flights_pb2.FlightsPerMonth(monthNumber=flights_pb2.MonthNumber(number=number_of_flights.month), flightsCount=number_of_flights.count)

    def GetNumberOfFlightsInMonths(self, request, context):
        numbers = []

        for data in request.monthNumbers:
            numbers.append(data.number)

        number_of_flights_in_months = self.repository.get_number_of_flights_in_months(month_numbers=numbers)

        grpc_number_of_flights_in_month = []

        for data in number_of_flights_in_months:
            grpc_number_of_flights_in_month.append(flights_pb2.FlightsPerMonth(monthNumber=flights_pb2.MonthNumber(number=data.month), flightsCount=data.count))

        return flights_pb2.FlightsInMonths(flightsPerMonth=grpc_number_of_flights_in_month)

    def GetTop10DestinationsForOrigin(self, request, context):
        number_of_flights_per_destination_at_origin = self.repository.get_top_10_destinations_for_origin(request.origin)
        grpc_number_of_flights_per_destination_at_origin = []

        for data in number_of_flights_per_destination_at_origin:
            grpc_number_of_flights_per_destination_at_origin.append(flights_pb2.FlightsPerDestination(numberOfFlights=data.numberOfFlights, destination=data.destination, origin=data.origin))

        return flights_pb2.DestinationResponse(flightsPerDestination=grpc_number_of_flights_per_destination_at_origin)

    def GetAirtimeAtOrigin(self, request, context):
        all_airtime_at_origin = self.repository.get_airtime_at_origin(request.origin)
        grpc_mean_airtime = []
        for data in all_airtime_at_origin:
            grpc_mean_airtime.append(data[0])
        print(grpc_mean_airtime)
        grpc_mean_airtime = np.array(grpc_mean_airtime)
        print(grpc_mean_airtime.dtype)
        grpc_mean_airtime = grpc_mean_airtime.astype('int32')
        print(grpc_mean_airtime)
        mean_airtime = np.mean(grpc_mean_airtime)

        return flights_pb2.AirtimeAtOrigin(air_time=mean_airtime, origin=request.origin)
