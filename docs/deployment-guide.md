\# Deployment Guide



\## 1. Provision Infrastructure

Terraform is used to provision:

\- VPC

\- Public subnet

\- Internet gateway

\- Route table

\- Security group

\- EC2 instance

\- S3 bucket



\## 2. Bootstrap EC2

The EC2 instance runs a user data script that:

\- updates packages

\- installs Python

\- installs pip

\- installs Nginx

\- starts the web server



\## 3. Deploy FastAPI App

After SSH access is configured:

\- create a Python virtual environment

\- install FastAPI, Uvicorn, and psutil

\- deploy the app code

\- run it using systemd



\## 4. Verify Endpoints

\- `/health`

\- `/system`

\- `/network-check`

\- `/report`

\- `/docs`



\## 5. Clean Up

Destroy resources after testing to avoid extra AWS cost.

