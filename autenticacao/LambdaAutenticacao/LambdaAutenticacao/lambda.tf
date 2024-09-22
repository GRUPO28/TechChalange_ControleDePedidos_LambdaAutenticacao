data "archive_file" "autenticacao" {
  type        = "zip"
  source_file = "Lambda/autenticacao.py"
  output_path = "files/autenticacao.zip"
}

resource "aws_lambda_function" "autenticacao" {
  function_name    = "autenticacao"
  role             = aws_iam_role.autenticacao.arn
  handler          = "autenticacao.lambda_handler"
  runtime          = "python3.9"
  timeout          = 10
  memory_size      = 128
  filename         = data.archive_file.autenticacao.output_path
  source_code_hash = data.archive_file.autenticacao.output_base64sha256

  vpc_config {
    subnet_ids         = data.aws_subnets.subnets.ids
    security_group_ids = data.aws_security_groups.security.ids
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
