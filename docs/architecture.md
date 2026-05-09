\# Architecture



\## High-Level Design

InfraPulse is a lightweight cloud operations platform built around a single AWS-hosted application server.



\### Main Components

\- Local development machine

\- Terraform

\- AWS VPC

\- Public subnet

\- Internet Gateway

\- Route table

\- Security Group

\- Ubuntu EC2 instance

\- FastAPI application

\- Nginx

\- systemd service

\- S3 bucket

\- IAM role and instance profile



\## Logical Flow

1\. Terraform provisions AWS resources.

2\. EC2 launches inside the public subnet.

3\. `user\_data.sh` bootstraps the server.

4\. FastAPI is installed and configured automatically.

5\. `systemd` keeps the application running persistently.

6\. Endpoints expose health, system, and network checks.

7\. The `/report` endpoint generates a JSON report.

8\. The EC2 IAM role allows the report to be uploaded securely to S3.



\## Security Design

\- SSH is restricted to a single public IP using `/32`

\- Port 80 is exposed for the landing page

\- Port 8000 is exposed for API access

\- S3 access is granted through an IAM role, not hardcoded credentials

\- Application dependencies are installed in a Python virtual environment



\## Visual Diagram



!\[InfraPulse Architecture](../architecture/infrapulse\_architecture\_diagram.svg)



\## Infrastructure Evidence



\### EC2 Running

!\[EC2 Running](../screenshots/09-ec2-instance-running-final.png)



\### Security Group Rules

!\[Security Group Rules](../screenshots/10-security-group-rules-final.png)



\### Networking Details

!\[Networking Details](../screenshots/11-instance-networking-details.png)



\## Suggested Diagram Layout

When presenting this project visually, use this structure:



Local Machine  

→ Terraform  

→ AWS Cloud  

→ VPC  

→ Public Subnet  

→ EC2 Instance  

→ FastAPI + Nginx + systemd  

→ S3 Upload



\## Example Architecture Description

InfraPulse provisions a dedicated AWS VPC with a public subnet and launches an Ubuntu EC2 instance. The instance is bootstrapped automatically using Terraform user data, which installs Python, Nginx, and the FastAPI application. The application exposes operational endpoints and uploads generated reports to Amazon S3 using an attached IAM role. This design demonstrates reproducible infrastructure provisioning, secure cloud integration, and automated operational reporting.

