from flask import Blueprint, make_response, request, jsonify
from .dao import DAOUser
from .modelo import User
import jwt
from datetime import datetime, timezone, timedelta

app_user = Blueprint('app_user', __name__)

module_name = 'user'
DAO_user = DAOUser()


key = 'CHAVE_s3cr3t4'


@app_user.route('/api/v1/authorization/token/', methods=['POST'])
def login():
    # exp é o tempo de expiração do token.
    # coloquei para 5 minutos a frente do tempo atual
    payload = {
        'username': request.form.get('username'),
        'exp': datetime.now(tz=timezone.utc) + timedelta(seconds=60*10)
    }
    #username será a primary key. Password não deverá ser passado no token de devolução
    user_verified = DAO_user.get_user(User(payload['username']))

    if user_verified is not None:
        token = jwt.encode(payload=payload, key=key)
        return jsonify({'token': token}), 200
    
    return make_response(jsonify({'Erro': 'Usuário ou senha inválidos'}), 400)  


@app_user.route('/api/v1/authorization/validation/', methods=['POST'])
def auth():
    try:
        # o token será passado na aba Headers do Insomnia. pra acessálo usarei a headers do request
        token = jwt.decode(request.form.get('authorization'), key, algorithms=['HS256'])
        user_verified = DAO_user.get_user(User(token['username']))
        # if user_verified is not None
        if user_verified is not None:
            return {}  # 200 token Válido
        else:
            raise Exception('user not found')
    except Exception as e:
        return make_response(jsonify({'Error': e.args[0]}), 401)
