from concurrent import futures
import grpc

import definitions.demo_pb2_grpc as demo_pb2_grpc
from service import DemoService, MyService


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    demo_pb2_grpc.add_DemoServiceServicer_to_server(
        DemoService(),
        server
    )

    demo_pb2_grpc.add_MyServiceServicer_to_server(
        MyService(),
        server
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("gRPC server running on port 50051")
    server.wait_for_termination()


def serve_secure():
    # server_credentials = grpc.ssl_server_credentials(
    #     [(private_key, certificate_chain)]
    # )
    server_credentials = grpc.local_server_credentials()

    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    demo_pb2_grpc.add_DemoServiceServicer_to_server(
        DemoService(),
        server
    )

    demo_pb2_grpc.add_MyServiceServicer_to_server(
        MyService(),
        server
    )

    server.add_secure_port("[::]:50051", server_credentials)
    server.start()

    print("Secure gRPC server running on port 50051")
    server.wait_for_termination()
