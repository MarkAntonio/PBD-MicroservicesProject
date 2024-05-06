from flask import Blueprint, make_response, request as flask_request, jsonify

from NotaPromissoria.PaymentClient.dao import DAOPaymentClient
from .dao import DAOPaymentContract
from .modelo import PaymentContract
import requests
import traceback


app_payment_contract = Blueprint(
    'app_payment_contract', __name__, url_prefix='/api/v1')
dao_payment_contract = DAOPaymentContract()
dao_payment_client = DAOPaymentClient()


@app_payment_contract.route('/payment-contract/', methods=['POST'])
def create_payment_contract():
    response = __authorize()

    if response.status_code == 200:
        str_date = flask_request.form.get("first_payment")
        payload = {
            "description": flask_request.form.get("description"),
            "value": float(flask_request.form.get("value")),
            "client_id": int(flask_request.form.get("client_id")),
            "number_months": int(flask_request.form.get("number_months")),
            "first_payment": PaymentContract.str_to_date(str_date)
        }
        try:
            payment_contract = PaymentContract(**payload)
            payment_id = dao_payment_contract.save(payment_contract)
            if payment_id is not None:
                # atribuindo id ao payment_contract para conseguir criar os payments_clients
                payment_contract.id = payment_id
                dao_payment_client.generate_payment_record(payment_contract)
                return jsonify({"id": payment_id})
            else:
                return make_response(jsonify({"Erro": "Campos obrigatórios"}), 400)
        except Exception as e:
            # desfaz a pré-alteração para conseguir fazer uso novamente da conexão da base.
            dao_payment_contract.rollback_transaction()
            traceback.print_exc()
            return make_response(jsonify({"Erro": e.args[0]}), 500)
    elif response.status_code == 401:
        return make_response(jsonify({'erro': 'Usuário não autorizado'}), 401)
    else:
        return make_response(response.json(), response.status_code)


@app_payment_contract.route('/payment-contract/<int:id>', methods=['PUT'])
def update_payment_contract(id: int):
    response = __authorize()

    if response.status_code == 200:
        contract_verified: PaymentContract = dao_payment_contract.get_by_id(id)
        if contract_verified is None:
            return make_response({"Erro": f"Não existe contrato com o id {id}"}, 404)

        str_date = flask_request.form.get("first_payment")
        payload = {
            "description": flask_request.form.get("description"),
            "value": float(flask_request.form.get("value")),
            "client_id": int(flask_request.form.get("client_id")),
            "number_months": int(flask_request.form.get("number_months")),
            "first_payment": PaymentContract.str_to_date(str_date)
        }

        updated_contract = PaymentContract(**payload, id=contract_verified.id)
        payment_clients_list = dao_payment_client.get_all_payments_by_contract_id(id)

        can_edit = True
        for payment in payment_clients_list:
            if payment['status'] not in ('PENDING', 'LATE'):
                can_edit = False
                break
           
        try:
            # caso não tenha sido pago, deleto os paymentClient e recrio.
            if can_edit:
                # deletando
                dao_payment_client.delete_all_by_contract_id(id)
                # criar
                dao_payment_client.generate_payment_record(updated_contract)
                # editar
                dao_payment_contract.update(updated_contract)

            else:
                # caso envie mais campos, retornar erro.
                valid_fields = 0
                for v in payload.values():
                    if v is not None:
                        valid_fields += 1

                if valid_fields > 1:
                    del payload['description']
                    fields = [field for field in payload.keys()]
                    return make_response(jsonify({"Erro": f"O contrato possui uma ou mais parcelas pagas, logo não é possível editar os campos: {fields}."}), 400)

                # caso já tenha sido pago, editar somente a descrição
                dao_payment_contract.update_description(updated_contract.description, id)

                
            return jsonify(updated_contract.get_json())
        
        except Exception as e:
            dao_payment_contract.rollback_transaction()
            traceback.print_exc()
            return make_response(jsonify({"Erro": e.args[0]}), 500)
    elif response.status_code == 401:
        return make_response(jsonify({'erro': 'Usuário não autorizado'}), 401)
    else:
        return make_response(response.json(), response.status_code)


@app_payment_contract.route('/payment-contract/', methods=['GET'])
def list_payment_contracts():
    response = __authorize()

    if response.status_code == 200:
        try:
            list_contracts = dao_payment_contract.get_all()
            return jsonify({"response :": list_contracts})
        except Exception as e:
            dao_payment_contract.rollback_transaction()
            traceback.print_exc()
            return make_response(jsonify({"Erro": e.args[0]}), 500)
    elif response.status_code == 401:
        return make_response(jsonify({'erro': 'Usuário não autorizado'}), 401)
    else:
        return make_response(response.json(), response.status_code)


def __authorize() -> requests.Response:
    token = {
        "authorization": flask_request.headers.get('authorization')
    }
    response = requests.post(
        url='http://localhost:5000/api/v1/authorization/validation/', data=token)
    return response


'''
@app_payment_contract.route('/payment-contract/', methods=['POST'])
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
            traceback.print_exc()
            return make_response(jsonify({"Erro": e.args[0]}), 500)
    elif response.status_code == 401:
        return make_response(jsonify({'erro': 'Usuário não autorizado'}), 401)
    else:
        return make_response(response.json(), response.status_code)'''