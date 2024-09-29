# Lambda de Autenticação do projeto Tech Chalange

## 1. Problema
Implementar um API Gateway e um function serverless para autenticar o cliente com base no CPF.
- Integrar ao sistema de autenticação para identificar o cliente.

## 2. Solução
Para suprir o necessário decidimos criar uma Lambda para cuidar do cadastro dos clientes. Por ela é possível também validar se o token é válido ou não.
<br></br>
Como a ideia do projeto não mudou a problematica, estar ou não autenticado / cadastrado não impedirá o uso dos outros recursos como fazer o pedido, para validar e atender ao solicitado, utilizamos a lambda enviando um POST com o token gerado para que seja validado.

## 3. Fluxo
A API Gateway recebe a requisição podendo ser:
- get -> Para autenticar, gerando um token e trazendo informações uteis.
- post -> Para validar o token gerado garantindo sua validade.
A lambda processará a requisição obtendo no DocumentDB de acordo com o que for solicitado.
<br></br>
![Fluxo](./assets/Diagrama.png)

