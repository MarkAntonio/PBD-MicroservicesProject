from flask import Blueprint, make_response, request, jsonify
from NotaPromissoria.client.dao import DAOClient
from NotaPromissoria.client.modelo import Client
import jwt

app_client = Blueprint('app_client', __name__)

module_name = 'client'
DAOClient = DAOClient()


key = 'CHAVE_s3cr3t4'

@app_client.route('/api/v1/clients/', methods=['GET'])
def get_client():
    clients = DAOClient.get_all()
    return make_response(jsonify(clients))


@app_client.route('/api/v1/clients/token/', methods=['POST'])
def login():
    payload = {
        'name': request.form.get('name')
    }
    print(payload)
    client_verified = DAOClient.get_Client(Client(payload['name']))

    if client_verified is not None:
        token = jwt.encode(payload=payload, key=key)
        return jsonify({'token': token}), 200
    
    return make_response(jsonify({'Error': 'Usuário ou senha inválidos'}), 400)  


@app_client.route('/api/v1/authorization/validation/', methods=['POST'])
def auth():
    return