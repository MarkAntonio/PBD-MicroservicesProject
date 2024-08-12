from typing import Self
from flask import Flask
from connect import ConnectDataBase
from PaymentContract.controler import app_payment_contract
from client.controller import app_client
from PaymentClient import DAOPaymentClient


app = Flask(__name__)
ConnectDataBase().init_table()
app.register_blueprint(app_payment_contract)
app.register_blueprint(app_client)



if __name__ == "__main__":
    app.run(debug=True, port=5001)


