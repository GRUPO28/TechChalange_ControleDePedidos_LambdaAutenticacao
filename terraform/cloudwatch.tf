resource "aws_cloudwatch_log_group" "lambda_watch" {
  name              = "/aws/lambda/${aws_lambda_function.function.function_name}"
  retention_in_days = 1
}