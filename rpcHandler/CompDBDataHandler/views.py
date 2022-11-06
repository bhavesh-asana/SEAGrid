import grpc
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.protobuf import json_format

import datacat_pb2_grpc
import datacat_pb2


# Create your views here.

def GetDataCatData(channel):
    stub = datacat_pb2_grpc.GridChemServiceStub(channel)
    rpc_log = stub.GetData(datacat_pb2.GetGridChemRequest())
    value_iterator = rpc_log.values()[0]
    data_type = type(rpc_log)
    print(data_type)
    return json_format.MessageToDict(value_iterator)


@csrf_exempt
def client(request):
    if request.method == "GET":
        print(request)
        with grpc.insecure_channel("localhost:50051") as channel:
            return JsonResponse(GetDataCatData(channel), safe=False)