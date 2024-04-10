from flask import Blueprint, make_response, request, jsonify
from user.dao import DAO_user
from user.modelo import User
import jwt

app_user = Blueprint('app_user', __name__)

module_name = 'user'
DAO_user = DAO_user()


key = 'CHAVE_s3cr3t4'


@app_user.route('/api/vi/authentication/token/', methods=['POST'])
def login():
    payload = {
        'name': request.form.get('name'),
        'password': request.form.get('password')
    }
    user_verified = DAO_user.get_user(User(payload['name'], payload['password']))
    if user_verified is not None:
        token = jwt.encode(payload=payload, key=key)
        return make_response(jsonify({'token': token}), 200)
    
    return make_response(jsonify({'Error': 'user not found'}), 400)
    

@app_user.route('/api/vi/authentication/', methods=['POST'])
def auth():
    try:
        jwt.decode(request.form.get('token'), key, algorithms=['HS256'])
        return {}  # 200 token Válido
    except Exception as e:
        return make_response(jsonify({'Error': e.args[0]}), 401)
