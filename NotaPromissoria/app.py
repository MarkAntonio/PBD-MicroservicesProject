from flask import Flask
from connect import ConnectDataBase
from client.controller import app_client


app = Flask(__name__)
ConnectDataBase().init_table()
app.register_blueprint(app_client)


if __name__ == "__main__":
    app.run(debug=True)
