from flask import Blueprint, make_response, request as flask_request, jsonify
from .dao import DAOPaymentContract
import requests


app_payment_contract = Blueprint('app_payment_contract', __name__)
dao_payment_contract = DAOPaymentContract()


@app_payment_contract.route('/api/v1/payment-contract/', methods=['POST'])
def create_payment_contract():

    payload = {
      "description": flask_request.form.get("description"),
      "value": flask_request.form.get("value"),
      "client_id": flask_request.form.get("client_id"),
      "number_months": flask_request.form.get("number_months"),
      "first_payment": flask_request.form.get("first_payment")
    }
    


