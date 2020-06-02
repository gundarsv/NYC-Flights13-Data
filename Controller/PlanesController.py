import Protos.planes_pb2_grpc as planes_pb2_grpc
import Protos.planes_pb2 as planes_pb2


def add_planes_controller_to_server(server, repository):
    planes_pb2_grpc.add_PlanesServicer_to_server(PlanesController(repository), server)


class PlanesController(planes_pb2_grpc.PlanesServicer):
    repository = None

    def __init__(self, repository):
        self.repository = repository

    def GetPlanes(self, request, context):
        all_planes = self.repository.get_all_planes()
        grpc_planes = []

        for data in all_planes:
            grpc_planes.append(planes_pb2.Plane(tailnum=data.tailnum, year=data.year, type=data.type, manufacturer=data.manufacturer, model=data.model,engines=data.engines, seats=data.seats, speed=data.speed, engine=data.engine))

        return planes_pb2.PlaneResponse(planes=grpc_planes)

    def GetManufacturersWithMoreThan200Planes(self, request, context):
        manufacturers_with_more_than_200_planes = self.repository.get_manufacturers_with_more_than_200_planes()
        grpc_manufacturers_with_more_than_200_planes = []

        for data in manufacturers_with_more_than_200_planes:
            grpc_manufacturers_with_more_than_200_planes.append(planes_pb2.Manufacturer(planes=data.planesTotal, manufacturer=data.manufacturer))

        return planes_pb2.ManufacturersResponse(manufacturers=grpc_manufacturers_with_more_than_200_planes)

    def GetNumberOfPlanesForEachManufacturerModel(self, request, context):
        number_of_planes_for_each_manufacturer_model = self.repository.get_number_of_planes_for_each_manufacturer_model(request.manufacturer)
        print(number_of_planes_for_each_manufacturer_model)
        grpc_number_of_planes_for_each_manufacturer_model = []

        for data in number_of_planes_for_each_manufacturer_model:
            grpc_number_of_planes_for_each_manufacturer_model.append(planes_pb2.NumberOfPlanesForModel(modelNumber=planes_pb2.ModelNumber(number=data.model),modelCount=data.count, manufacturer=data.manufacturer))

        return planes_pb2.NumberOfPlanesForModelResponse(numberOfPlanesForModel = grpc_number_of_planes_for_each_manufacturer_model)