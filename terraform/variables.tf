variable "aws_region" {
  description = "AWS region for the project"
  type        = string
}

variable "project_name" {
  description = "Project name prefix"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
}

variable "web_ingress_cidr" {
  description = "CIDR allowed to access the web server"
  type        = string
}

variable "app_port" {
  description = "Internal application port"
  type        = number
}

variable "s3_force_destroy" {
  description = "Allow Terraform to delete the S3 bucket even if it contains files"
  type        = bool
}

variable "availability_zone" {
  description = "Preferred availability zone for the public subnet"
  type        = string
}

variable "key_name" {
  description = "Existing EC2 key pair name"
  type        = string
}

variable "ssh_ingress_cidr" {
  description = "CIDR allowed to access SSH"
  type        = string
}