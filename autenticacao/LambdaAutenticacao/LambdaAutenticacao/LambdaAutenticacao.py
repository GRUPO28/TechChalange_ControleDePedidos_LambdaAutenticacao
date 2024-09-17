import json

cpf_storage = {}

def lambda_handler(event, context):
    method = event.get('httpMethod')
    cpf = event.get('cpf')

    if method == 'POST':
        return handle_post(cpf)
    elif method == 'GET':
        return handle_get(cpf)
    elif method == 'DELETE':
        return handle_delete(cpf)
    else:
        return {
            'statusCode': 405,
            'body': json.dumps('Method Not Allowed')
        }

def handle_post(cpf):
    if is_valid_cpf(cpf):
        cpf_storage[cpf] = True
        return {
            'statusCode': 201,
            'body': json.dumps(f'CPF added {cpf}')
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('CPF invalid')
        }

def handle_get(cpf):
    if is_valid_cpf(cpf):
        if cpf in cpf_storage:
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
        if cpf in cpf_storage:
            del cpf_storage[cpf]
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
    if len(cpf) != 11:
        return False
    return True