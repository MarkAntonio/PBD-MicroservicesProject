from flask import Blueprint, make_response, request as flask_request, jsonify
from .dao import DAOClient
import requests
import traceback


app_client = Blueprint('app_client', __name__)
DAOClient = DAOClient()


@app_client.route('/api/v1/clients/', methods=['GET'])
def get_client():
    try:
        payload = {
            "authorization": flask_request.headers.get('authorization')
            }
        response = requests.post(url='http://localhost:5000/api/v1/authorization/validation/', data=payload)
        
        if response.status_code == 200:
            clients = DAOClient.get_all()    
            return jsonify({"response": clients})
        elif response.status_code == 401:
            return make_response(jsonify({'erro': 'Usuário não autorizado'}), 401)
        else:
            return make_response(response.json(), response.status_code)
    except Exception as e:
        traceback.print_exc()
        return make_response(jsonify({"Erro": e.args[0]}), 500)
