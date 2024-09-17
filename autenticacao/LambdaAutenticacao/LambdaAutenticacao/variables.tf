variable "aws_region" {
  description = "AWS region"
  default     = "sa-east-1"
}

variable "aws_profile" {
  type		  = string
  description = "AWS profile"
  default     = "default"
}

variable "instance_type" {
  type        = string
  description = "Instance type"
}

variable "enviroment" {
  type        = string
  description = "Environment"
  default     = "dev"
}