terraform {
  required_version = ">= 0.12"

  backend "s3" {
    bucket = "tf-windowspaulojunior"
    key    = "LambdaAutenticacao/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Owner     = "Paulo Junior"
      CreatedAt = "2024-09-11"
      ManagedBy = "Terraform"
    }
  }
}