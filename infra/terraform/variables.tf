variable "aws_region" {
  description = "AWS region to deploy into."
  type        = string
  default     = "ap-south-1"
}

variable "name" {
  description = "Name prefix for all resources."
  type        = string
  default     = "nyc-analytics"
}

variable "allowed_cidrs" {
  description = "CIDR blocks allowed to reach the dashboard on port 8501, for example [\"203.0.113.10/32\"]. No default on purpose, so the dashboard is never open to the world by accident."
  type        = list(string)
}

variable "instance_type" {
  description = "EC2 instance type for the dashboard host."
  type        = string
  default     = "t3.small"
}

variable "db_instance_class" {
  description = "RDS instance class."
  type        = string
  default     = "db.t4g.micro"
}

variable "db_allocated_storage" {
  description = "RDS storage in GiB. Increase before loading the full TLC dataset."
  type        = number
  default     = 20
}

variable "db_engine_version" {
  description = "PostgreSQL major version."
  type        = string
  default     = "16"
}

variable "db_name" {
  description = "Database name."
  type        = string
  default     = "transportation_analytics"
}

variable "db_username" {
  description = "Master username. The password is generated and kept in AWS Secrets Manager."
  type        = string
  default     = "analytics"
}

variable "db_deletion_protection" {
  description = "Protect the database from accidental deletion."
  type        = bool
  default     = false
}

variable "repo_url" {
  description = "Git repository the instance clones and builds."
  type        = string
  default     = "https://github.com/Codewith-Megha/NYC-Transportation-Analytics"
}

variable "repo_branch" {
  description = "Branch to deploy."
  type        = string
  default     = "main"
}
