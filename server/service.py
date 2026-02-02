import definitions.demo_pb2 as demo_pb2
import definitions.demo_pb2_grpc as demo_pb2_grpc

class DemoService(demo_pb2_grpc.DemoServiceServicer):

    def IsTrue(self, request, context):
        value = request.value

        is_positive = value >= 0

        return demo_pb2.DemoResponse(
            is_true = is_positive
        )
