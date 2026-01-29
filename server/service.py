import definitions.demo_pb2 as demo_pb2
import definitions.demo_pb2_grpc as demo_pb2_grpc

class DemoService(demo_pb2_grpc.DemoServiceServicer):

    def DemoService(self, request, context):
        value = request.value

        is_positive = value >= 0

        return demo_pb2.IsTrue(
            is_true = is_positive
        )
