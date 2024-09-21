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
    subnet_ids         = var.subnet_ids
    security_group_ids = var.security_group_ids
  }
}



variable "vpc_id" {
  description = "ID da VPC onde a Lambda será executada"
  type        = string
  default     = "vpc-0a212b86487fd4a9b" # Altere para o ID da sua VPC
}

variable "subnet_ids" {
  description = "IDs das sub-redes onde a Lambda terá acesso"
  type        = list(string)
  default     = ["subnet-01ebc2e58347169e1", "subnet-0e07230d21a480155", "subnet-02613bc56beb311e9"] # Altere para os IDs das suas sub-redes
}

variable "security_group_ids" {
  description = "IDs dos grupos de segurança que a Lambda usará"
  type        = list(string)
  default     = ["sg-07cb158bd1ee75cee"] # Altere para o ID do seu grupo de segurança
}
