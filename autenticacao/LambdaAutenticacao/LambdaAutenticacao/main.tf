terraform {
  required_version = ">= 0.12"

  backend "s3" {
	bucket = "tf-windowspaulojunior"
	key    = "LambdaAutenticacao/terraform.tfstate"
	region = var.aws_region
	profile = "tf_windowsp_paulojunior"
  }
}

provider "aws" {
  region = var.aws_region
  profile = "tf_windowsp_paulojunior"

  default_tags {
  tags = {	
			Owner		= "Paulo Junior"
			CreatedAt	=	"2024-09-11"
			ManagedBy	=	"Terraform"
		}
	}
}