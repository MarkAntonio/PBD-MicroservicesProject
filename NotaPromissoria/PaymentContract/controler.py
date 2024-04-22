from flask import Blueprint, make_response, request as flask_request, jsonify
from .dao import DAOPaymentContract
from .modelo import PaymentContract
import requests


app_payment_contract = Blueprint('app_payment_contract', __name__)
dao_payment_contract = DAOPaymentContract()


@app_payment_contract.route('/api/v1/payment-contract/', methods=['POST'])
def create_payment_contract():

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


    
