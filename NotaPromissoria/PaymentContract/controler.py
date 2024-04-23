from flask import Blueprint, make_response, request as flask_request, jsonify
from .dao import DAOPaymentContract
from .modelo import PaymentContract
import requests


app_payment_contract = Blueprint('app_payment_contract', __name__)
dao_payment_contract = DAOPaymentContract()


@app_payment_contract.route('/api/v1/payment-contract/', methods=['POST'])
def create_payment_contract():
    response = __authorize()

    if response.status_code == 200:
        str_date = flask_request.form.get("first_payment")
        payload = {
            "description": flask_request.form.get("description"),
            "value": flask_request.form.get("value"),
            "client_id": flask_request.form.get("client_id"),
            "number_months": flask_request.form.get("number_months"),
            "first_payment": PaymentContract.str_to_date(str_date)
        }
        try:
            payment_id = dao_payment_contract.save(PaymentContract(**payload))
            if payment_id:
                return jsonify({"id": payment_id})
            else:
                return make_response(jsonify({"Erro": "Campos obrigatórios"}), 400)
        except Exception as e:
            # desfaz a pré-alteração para conseguir fazer uso novamente da conexão da base.
            dao_payment_contract.rollback_transaction()
            return make_response(jsonify({"Erro": e.args[0]}), 500)
    elif response.status_code == 401:
        return make_response(jsonify({'erro': 'Usuário não autorizado'}), 401)
    else:
        return make_response(response.json(), response.status_code)


@app_payment_contract.route('/api/v1/payment-contract/<int:id>', methods=['PUT'])
def update_payment_contract(id: int):
    response = __authorize()

    if response.status_code == 200:
        contract_verified: PaymentContract = dao_payment_contract.get_by_id(id)
        if not contract_verified:
            return make_response({"Erro": f"Não existe contrato com o id {id}"}, 404)
        
        str_date = flask_request.form.get("first_payment")
        payload = {
            "description": flask_request.form.get("description"),
            "value": flask_request.form.get("value"),
            "client_id": flask_request.form.get("client_id"),
            "number_months": flask_request.form.get("number_months"),
            "first_payment": PaymentContract.str_to_date(str_date)
        }
        
        updated_contract = PaymentContract(**payload, id=contract_verified.id)
        
        try:
            dao_payment_contract.update(updated_contract)
            return jsonify({"pay": updated_contract.get_json()})
        except Exception as e:
            return make_response(jsonify({"Erro": e.args[0]}), 500)
        
    return make_response(response.json(), response.status_code)


def __authorize() -> requests.Response:
    token = {
        "authorization": flask_request.headers.get('authorization')
    }
    response = requests.post(url='http://localhost:5000/api/v1/authorization/validation/', data=token)
    return response

    
