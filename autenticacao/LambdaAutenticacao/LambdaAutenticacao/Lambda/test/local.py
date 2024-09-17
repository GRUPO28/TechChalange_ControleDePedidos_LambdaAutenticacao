import json
from LambdaAutenticacao import lambda_handler

def test_post():
    event = {
        'httpMethod': 'POST',
        'cpf': '12345678901'
    }
    response = lambda_handler(event, None)
    print('POST Response:', response)

def test_get():
    event = {
        'httpMethod': 'GET',
        'cpf': '12345678901'
    }
    response = lambda_handler(event, None)
    print('GET Response:', response)

def test_delete():
    event = {
        'httpMethod': 'DELETE',
        'cpf': '12345678901'
    }
    response = lambda_handler(event, None)
    
    print('DELETE Response:', response)

if __name__ == '__main__':
    print("Teste POST ")
    test_post()
    
    print("\nTeste GET")
    test_get()
    
    print("\nTeste DELETE")
    test_delete()
    
    print("\nTeste GET")
    test_get()