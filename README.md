# CDK ECS Fargate Deployment with Secrets Manager

This project demonstrates a secure, production-ready deployment of a containerized application using AWS CDK in Python. It provisions a VPC, ECS Fargate cluster, and deploys a Dockerized NGINX container with secrets injected from AWS Secrets Manager.

---

## ✅ Features

- AWS CDK (Python)
- ECS Fargate cluster
- NGINX container from public registry
- Secrets injected from AWS Secrets Manager
- CloudWatch log streaming
- Public IP access

---

## 🧱 Stack Components

- `aws_ec2.Vpc`: Private/public subnets
- `aws_ecs.Cluster`: Managed ECS Fargate cluster
- `aws_secretsmanager.Secret`: Mock secret created via CDK
- `aws_ecs.FargateService`: Docker container with exposed port 80

---

## 🔒 Secret Injection

```python
secrets={
  "APP_SECRET": ecs.Secret.from_secrets_manager(secret)
}

