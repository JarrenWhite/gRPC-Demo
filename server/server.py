from concurrent import futures
import grpc

import protobufs.demo_pb2_grpc
from service import DemoService


def serve():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )

    demo_pb2_grpc.add_DemoServiceServicer_to_server(
        DemoService(),
        server
    )

    server.add_insecure_port("[::]:50051")
    server.start()

    print("gRPC server running on port 50051")
    server.wait_for_termination()
