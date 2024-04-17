from flask import Flask
from connect import ConnectDataBase
from user.controller import app_user


app = Flask(__name__)
ConnectDataBase().init_table()
app.register_blueprint(app_user)


if __name__ == "__main__":
    app.run(debug=True)
            