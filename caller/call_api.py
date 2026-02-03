import grpc
import definitions.demo_pb2 as demo_pb2
import definitions.demo_pb2_grpc as demo_pb2_grpc


def call_is_true(value: int) -> bool:
    channel_credentials = grpc.local_channel_credentials()

    with grpc.secure_channel("localhost:50051", channel_credentials) as channel:
        stub = demo_pb2_grpc.DemoServiceStub(channel)

        request = demo_pb2.DemoRequest(value=value)

        response = stub.IsTrue(request)

        return response.is_true


if __name__ == "__main__":
    print(call_is_true(5))
