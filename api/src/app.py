import json
from flask import Flask

from routes.commercial_bank import commercial_bank_route

app = Flask(__name__)

app.register_blueprint(commercial_bank_route)

if __name__ == "__main__":
    app.run(debug=True)