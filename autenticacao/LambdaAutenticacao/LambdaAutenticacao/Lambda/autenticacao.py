import json
import os
from pymongo import MongoClient

storage = {}

retorno = {
    'statusCode': 400,
    'body': json.dumps('Invalid data.')
}

# Conecte-se ao Amazon DocumentDB
client = MongoClient(os.getenv('DB_CONECTION_STRING'))
db = client[os.getenv('DB_DATABASE')]
collection = db[os.getenv('DB_COLLECTION')]

def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method")


    if method == 'POST':
        return handle_post(event)
    elif method == 'GET':
        return handle_get(event)
    else:
        retorno['statusCode'] = 405
        retorno['body'] = json.dumps('Method Not Allowed')

def handle_post(event):

    if event.get("body"):
        body = json.loads(event["body"])
        cpf = body.get("cpf")
        email = body.get("email")
        nome = body.get("nome")
    else:
        cpf = None

    if cpf.strip():
        cpf = cpf.strip().replace(".", "").replace("-", "")
        result = collection.find_one({'CPF': cpf})
        
        if result is not None:
            retorno['body'] = json.dumps(f'CPF {cpf} alredy exists')
            return retorno
            
        if is_valid_cpf(cpf):
            retorno['statusCode'] = 201
            retorno['body'] = json.dumps(f'CPF {cpf}')
        else:
             retorno['body'] = json.dumps('CPF invalid')
             return retorno
    else:
        retorno['body'] = json.dumps('CPF invalid')
        return retorno
         
    if email.strip():
        if is_valid_email(email):
            retorno['body'] += json.dumps(f' e-mail {email} and {nome} added')
        else:
            retorno['body'] = json.dumps(f'The e-mail {email} is invalid')
            return retorno
    else:
        retorno['body'] = json.dumps(f'The e-mail {email} is invalid')
        return retorno
        
    if nome.strip():
        retorno['body'] += json.dumps(f' and {nome} added')
    else:
        retorno['body'] = json.dumps(f'The name {nome} is invalid')
        return retorno
    
    
    storage[cpf] = {'CPF': cpf, 'Nome': nome, 'Email': email}
    collection.insert_one({'CPF': cpf, 'Nome': nome, 'Email': email})
        
    return retorno
                 
    

def handle_get(event):

    cpf = event.get("queryStringParameters", {}).get("cpf")
    if is_valid_cpf(cpf):
        if cpf in storage:
            retorno['statusCode'] = 200
            retorno['body'] = json.dumps(f'CPF found {cpf}')
            return retorno
        else:
            retorno['statusCode'] = 404
            retorno['body'] = json.dumps(f'CPF not found')
            return retorno
    else:
        return retorno

def is_valid_cpf(cpf: str) -> bool:    
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