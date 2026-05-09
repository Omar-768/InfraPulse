output "instance_public_ip" {
  description = "Public IP of the EC2 instance"
  value       = aws_instance.app_server.public_ip
}

output "instance_public_dns" {
  description = "Public DNS of the EC2 instance"
  value       = aws_instance.app_server.public_dns
}

output "s3_bucket_name" {
  description = "S3 bucket name for reports"
  value       = aws_s3_bucket.reports.bucket
}

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}