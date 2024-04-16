from flask import Blueprint, make_response, request as flask_request, jsonify
from dao import DAOClient

import requests
import jwt


key = 'CHAVE_s3cr3t4'

app_test = Blueprint("test", __name__)


@app_test.route('/test/')
def test():
    # consultando uma API
    return make_response(requests.get('https://pokeapi.co/api/v2/pokemon/ditto').json())


@app_test.route('/postit/', methods=["POST"])
def test2():
    print(flask_request.get_json())
    a = flask_request.get_json()
    a["Ai"] = "Bixo lindo"
    return a


@app_test.route('/login/', methods=['POST'])
def login():
    response = requests.post(
        'http://localhost:5000/api/v1/authorization/token/', data=flask_request.get_json())
    return make_response(jsonify(response.json()))


@app_test.route('/api/v1/clients/', methods=['GET'])
def get_clients():
    header = {
        "token": flask_request.headers.get('authorization')
        }
    response = requests.post(url='http://localhost:5000/api/v1/authorization/validation/', headers=header)
    
    if response.status_code == 200:
        return DAOClient().get_client()
    elif response.status_code == 401:
        return make_response(jsonify({'error': 'user not authorized'}, 401))
    else:
        return make_response(response.json(), response.status_code)
