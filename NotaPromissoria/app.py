from flask import Flask
from connect import ConnectDataBase
from client.controller import app_client
from PaymentContract.controler import app_payment_contract


app = Flask(__name__)
ConnectDataBase().init_table()
app.register_blueprint(app_client)
app.register_blueprint(app_payment_contract)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
