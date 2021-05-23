import json
from flask import Flask
from flask_cors import CORS

from routes.commercial_bank import commercial_bank_route

app = Flask(__name__)
CORS(app)

app.register_blueprint(commercial_bank_route)

if __name__ == "__main__":
    app.run(debug=True)