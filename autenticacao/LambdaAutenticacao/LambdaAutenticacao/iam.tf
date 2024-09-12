resource "aws_iam_role" "autenticacao" {
  name = "autenticacao"
  assume_role_policy = jsonencode({
	Version = "2012-10-17"
	Statement = [
	  {
		Effect = "Allow"
		Principal = {
		  Service = "lambda.amazonaws.com"
		}
		Action = "sts:AssumeRole"
	  }
	]
  })
}