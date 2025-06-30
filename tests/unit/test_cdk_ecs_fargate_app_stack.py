import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_ecs_fargate_app.cdk_ecs_fargate_app_stack import CdkEcsFargateAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_ecs_fargate_app/cdk_ecs_fargate_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkEcsFargateAppStack(app, "cdk-ecs-fargate-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
