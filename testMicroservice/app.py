from flask import Flask
from controller import app_test

app = Flask(__name__)
app.register_blueprint(app_test)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
