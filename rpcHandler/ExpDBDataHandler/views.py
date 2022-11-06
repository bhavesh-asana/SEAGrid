import grpc
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.protobuf import json_format

import molecule_pb2
import molecule_pb2_grpc


# Create your views here.
def GetMoleculeData(channel):
    stub = molecule_pb2_grpc.MoleculeServiceStub(channel)
    rpc_log = stub.GetMolecule(molecule_pb2.GetMoleculeRequest())
    value_iterator = rpc_log.values()[0]
    data_type = type(rpc_log)
    print(data_type)
    return json_format.MessageToDict(value_iterator)


@csrf_exempt
def client(request):
    if request.method == "GET":
        print(request)
        with grpc.insecure_channel("localhost:50051") as channel:
            # Return the JSON Object stream
            return JsonResponse(GetMoleculeData(channel), safe=False)