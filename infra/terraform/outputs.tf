output "dashboard_url" {
  description = "Dashboard address. Allow a minute or two after apply for the instance to build and start."
  value       = "http://${aws_instance.app.public_ip}:8501"
}

output "instance_id" {
  description = "Use with: aws ssm start-session --target <id>"
  value       = aws_instance.app.id
}

output "db_endpoint" {
  description = "RDS endpoint (private, reachable only from the dashboard host)."
  value       = aws_db_instance.this.endpoint
}

output "db_secret_arn" {
  description = "Secrets Manager secret holding the generated database credentials."
  value       = aws_db_instance.this.master_user_secret[0].secret_arn
}
