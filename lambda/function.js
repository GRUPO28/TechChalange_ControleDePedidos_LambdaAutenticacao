const { MongoClient } = require('mongodb');
const jwt = require('jsonwebtoken');

const uri = process.env.DB_CONNECTION_STRING;
const secret = process.env.JWT_SECRET;

exports.handler = async (event) => {
    console.log('Event: ', event);
    
    let responseMessage = '';
    let statusCode = 200;

    try {
        // Conectando ao DocumentDB
        const client = new MongoClient(uri, { 
            useNewUrlParser: true, 
            useUnifiedTopology: true,
            retryWrites: false // Desativa retryable writes
        });
        await client.connect();
        
        // Selecionando o banco de dados e a coleção
        const db = client.db('controlePedidosDB');
        const collection = db.collection('cadastros');

        if (event.httpMethod === 'GET') {
            const { cpf } = event.queryStringParameters;

            if (!cpf) {
                await client.close();
                return {
                    statusCode: 400,
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        message: 'CPF não fornecido na requisição'
                    }),
                };
            }

            // Procura o cliente pelo CPF informado
            const clientData = await collection.findOne({ cPF: cpf });

            if (clientData) {
                // Gerar o token com base no CPF
                const token = jwt.sign({ cpf: clientData.cPF }, secret, { expiresIn: '1h' });

                responseMessage = `Cliente encontrado: ${clientData.nome}. Token gerado.`;

                await client.close();
                return {
                    statusCode: 200,
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        message: responseMessage,
                        token: token,
                        client: clientData
                    }),
                };
            } else {
                responseMessage = `Nenhum cliente encontrado com o CPF ${cpf}`;
                statusCode = 404;
            }

            await client.close();
            return {
                statusCode,
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    message: responseMessage
                }),
            };
        }

        if(event.httpMethod === 'POST'){

            const body = JSON.parse(event.body);
            const token = body.token;  // Extraindo o token do corpo da requisição
            
            // Verifica o token JWT
            const decoded = jwt.verify(token, secret);
            console.log('Token verificado com sucesso:', decoded);

            responseMessage = 'Token válido.' + decoded;
            // Você pode adicionar lógica adicional aqui, como salvar algo no banco de dados ou retornar mais dados
        }

        await client.close();

        return {
            statusCode,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: responseMessage
            }),
        };
    } catch (err) {
        console.error('Error:', err);

        return {
            statusCode: 500,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                message: 'Internal Server Error',
                error: err.message
            }),
        };
    }
};
