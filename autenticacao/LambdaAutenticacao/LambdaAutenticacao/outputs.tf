output "lambdas" {
  value = [{ 
	arn = aws_lambda_function.autenticacao.arn
	name = aws_lambda_function.autenticacao.function_name
	version = aws_lambda_function.autenticacao.version
	description = aws_lambda_function.autenticacao.description
	last_modified = aws_lambda_function.autenticacao.last_modified
	}]
}
