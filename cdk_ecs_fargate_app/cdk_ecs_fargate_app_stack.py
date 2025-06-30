from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_logs as logs,
    aws_secretsmanager as secretsmanager,
)
from constructs import Construct

class CdkEcsFargateAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1. VPC
        vpc = ec2.Vpc(self, "MyVpc", max_azs=2)

        # 2. ECS Cluster
        cluster = ecs.Cluster(self, "MyCluster", vpc=vpc)

        # 3. Secrets Manager secret (auto-created for demo purposes)
        secret = secretsmanager.Secret(self, "AppSecret", secret_name="MyAppSecret")

        # 4. Fargate Task Definition
        task_def = ecs.FargateTaskDefinition(self, "MyTaskDef")

        container = task_def.add_container(
            "MyContainer",
            image=ecs.ContainerImage.from_registry("nginx"),  # public nginx image
            memory_limit_mib=512,
            logging=ecs.LogDriver.aws_logs(
                stream_prefix="ecs-logs",
                log_retention=logs.RetentionDays.ONE_DAY
            ),
            environment={
                "APP_ENV": "production"
            },
            secrets={
                "APP_SECRET": ecs.Secret.from_secrets_manager(secret)
            }
        )

        container.add_port_mappings(
            ecs.PortMapping(container_port=80)
        )

        # 5. Fargate Service (with public IP)
        ecs.FargateService(self, "MyFargateService",
            cluster=cluster,
            task_definition=task_def,
            desired_count=1,
            assign_public_ip=True
        )

