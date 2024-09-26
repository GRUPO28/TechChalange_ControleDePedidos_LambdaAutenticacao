data "archive_file" "lambda" {
  type = "zip"

  source_dir  = "../${path.module}/lambda"
  output_path = "../${path.module}/lambda.zip"
}

resource "aws_lambda_function" "function" {
  function_name = "function"
  runtime       = "nodejs16.x"
  handler       = "function.handler"

  filename         = data.archive_file.lambda.output_path
  source_code_hash = data.archive_file.lambda.output_base64sha256

  role = aws_iam_role.lambda_exec.arn

  vpc_config {
    subnet_ids         = data.aws_subnets.subnets.ids
    security_group_ids = data.aws_security_groups.security.ids
  }

  environment {
    variables = {
      DB_CONNECTION_STRING = var.DB_CONNECTION_STRING
      JWT_SECRET           = var.JWT_SECRET
    }
  }
}


data "aws_vpc" "default-vpc" {
  filter {
    name   = "tag:Name"
    values = ["default-us-east-1"]
  }
}

data "aws_subnets" "subnets" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default-vpc.id]
  }
}

data "aws_security_groups" "security" {
  filter {
    name   = "vpc-id"
    values = [data.aws_vpc.default-vpc.id]
  }
}
