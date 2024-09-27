variable "region" {
  default = "us-east-1"
}

variable "name" {
  default = "api"
}

variable "DB_CONNECTION_STRING" {
  description = "The connection string for the database"
  type        = string
}

variable "JWT_SECRET" {
  description = "Secret for JWT"
  type        = string
}