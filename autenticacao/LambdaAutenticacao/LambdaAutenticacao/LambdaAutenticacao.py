import json

storage = {}

retorno = {
    'statusCode': None,
    'body': None
}

def lambda_handler(event, context):
    method = event.get('httpMethod')
    cpf = event.get('cpf')
    name = event.get('nome')
    email = event.get('email')

    if method == 'POST':
        return handle_post(cpf, name, email)
    elif method == 'GET':
        return handle_get(cpf)
    elif method == 'DELETE':
        return handle_delete(cpf)
    else:
        retorno['statusCode'] = 405
        retorno['body'] = json.dumps('Method Not Allowed')

def handle_post(cpf, name, email):
    
    if cpf.strip():
        if is_valid_cpf(cpf):
            retorno['statusCode'] = 201
            retorno['body'] = json.dumps(f'CPF added {cpf}')
    else:
         retorno['statusCode'] = 400
         retorno['body'] = json.dumps('CPF invalid')
         return retorno
         
    if email.strip():
        if is_valid_email(email):
            retorno['statusCode'] = 201
            retorno['body'] += json.dumps(f' e-mail {email} and {name} added')
    else:
        retorno['statusCode'] = 400
        retorno['body'] = json.dumps(f'e-mail {email} and {name} are invalid')
        return retorno
    
    storage[cpf, name, email] = True
        
    return retorno
                 
    

def handle_get(cpf):
    if is_valid_cpf(cpf):
        if cpf in storage:
            return {
                'statusCode': 200,
                'body': json.dumps(f'CPF found {cpf}')
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('CPF not found')
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('CPF invalid')
        }

def handle_delete(cpf):
    if is_valid_cpf(cpf):
        if cpf in storage:
            del storage[cpf]
            return {
                'statusCode': 200,
                'body': json.dumps('CPF deleted')
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('CPF not found')
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('CPF invalid')
        }

def is_valid_cpf(cpf: str) -> bool:
    cpf = cpf.strip().replace(".", "").replace("-", "")
    
    if len(cpf) != 11:
        return False
    
    multiplicador1 = [ 10, 9, 8, 7, 6, 5, 4, 3, 2 ]
    multiplicador2 = [ 11, 10, 9, 8, 7, 6, 5, 4, 3, 2 ]
    
    temp_cpf = cpf[:9]
    soma = sum(int(temp_cpf[i]) * multiplicador1[i] for i in range(9))
    resto = soma % 11
           
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
      
    temp_cpf += str(digito1)
    soma = sum(int(temp_cpf[i]) * multiplicador2[i] for i in range(10))
    resto = soma % 11
    
    if(resto < 2):
        digito2 = 0
    else:
        digito2 = 11 - resto
     
    temp_cpf += str(digito2)
    
    return cpf == temp_cpf

def is_valid_email(email: str) -> bool:
    return "@" in email
        