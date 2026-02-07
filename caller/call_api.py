import grpc
import definitions.demo_pb2 as demo_pb2
import definitions.demo_pb2_grpc as demo_pb2_grpc

from typing import Tuple


def call_is_true(value: int) -> bool:
    channel_credentials = grpc.local_channel_credentials()

    with grpc.secure_channel("localhost:50051", channel_credentials) as channel:
        stub = demo_pb2_grpc.DemoServiceStub(channel)

        request = demo_pb2.DemoRequest(value=value)

        response = stub.IsTrue(request)

        return response.is_true


def call_my_service_api(value_one, value_two) -> Tuple[int, int, int]:
    channel_credentials = grpc.local_channel_credentials()

    with grpc.secure_channel("localhost:50051", channel_credentials) as channel:
        stub = demo_pb2_grpc.MyServiceStub(channel)

        request = demo_pb2.MyServiceRequest(
            value_one=value_one,
            value_two=value_two
        )

        response = stub.MyServiceApi(request)

        return response.sum, response.product, response.difference


if __name__ == "__main__":
    print(call_is_true(5))

    api_sum, api_product, api_difference = call_my_service_api(3, 5)
    print(api_sum)
    print(api_product)
    print(api_difference)
