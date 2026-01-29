import protobufs.demo_pb2
import protobufs.demo_pb2_grpc

class DemoService(demo_pb2_grpc.DemoServiceServicer):

    def DemoService(self, request, context):
        value = request.value

        is_positive = value >= 0

        return demo_pb2.DemoResponse(
            is_true = is_positive
        )
