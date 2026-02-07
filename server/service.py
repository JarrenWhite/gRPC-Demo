import definitions.demo_pb2 as demo_pb2
import definitions.demo_pb2_grpc as demo_pb2_grpc

class DemoService(demo_pb2_grpc.DemoServiceServicer):

    def IsTrue(self, request, context):
        value = request.value

        is_positive = value >= 0

        return demo_pb2.DemoResponse(
            is_true = is_positive
        )

class MyService(demo_pb2_grpc.MyServiceServicer):

    def MyServiceApi(self, request, context):
        value_one = request.value_one
        value_two = request.value_two

        return demo_pb2.MyServiceResponse(
            sum = value_one + value_two,
            product = value_one * value_two,
            difference = value_one - value_two
        )

    def SecondMyService(self, request, context):
        sum = request.sum
        product = request.product
        difference = request.difference

        return demo_pb2.MyServiceRequest(
            value_one = sum,
            value_two = product + difference
        )
