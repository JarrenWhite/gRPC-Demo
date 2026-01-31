from concurrent import futures
import grpc

import definitions.demo_pb2_grpc as demo_pb2_grpc
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


def serve_secure():
    private_key = b"""
    -----BEGIN EC PRIVATE KEY-----
    MHcCAQEEIA4qK+z0DemoKeyForGrpcOnly8NhqG7k8a1joAoGCCqGSM49
    AwEHoUQDQgAEuW2RZ0pniS3pSkeY8a3R5wK3z4+F9y1ZKkYxQw==
    -----END EC PRIVATE KEY-----
    """

    certificate_chain = b"""
    -----BEGIN CERTIFICATE-----
    MIIBpDCCAUqgAwIBAgIUDemoCertForGrpcOnlyMAoGCCqGSM49BAMC
    MBUxEzARBgNVBAMMCmxvY2FsaG9zdDAeFw0yNjAxMzEwMDAwMDBa
    Fw0yNzAxMzEwMDAwMDBaMBUxEzARBgNVBAMMCmxvY2FsaG9zdDBZ
    MBMGByqGSM49AgEGCCqGSM49AwEHA0IABLltkWdKZ4kt6UpHmPGt
    0ecCt8+PhfctWSpGMUMwCgYIKoZIzj0EAwIDSAAwRQIhANf+Demo
    FakeButStructurallyValid==
    -----END CERTIFICATE-----
    """

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

    server.add_secure_port("[::]:50051", server_credentials)
    server.start()

    print("Secure gRPC server running on port 50051")
    server.wait_for_termination()
