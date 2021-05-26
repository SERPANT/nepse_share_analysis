import json
from flask import Flask
from flask_cors import CORS

from routes.share_info import share_info_route

app = Flask(__name__)
CORS(app)

app.register_blueprint(share_info_route)

if __name__ == "__main__":
    app.run(debug=True)