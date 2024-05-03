from flask import Flask
from NotaPromissoria.connect import ConnectDataBase
from NotaPromissoria.PaymentContract.controler import app_payment_contract
from NotaPromissoria.client.controller import app_client

app = Flask(__name__)
ConnectDataBase().init_table()
app.register_blueprint(app_payment_contract)
app.register_blueprint(app_client)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
