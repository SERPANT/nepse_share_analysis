import json
from flask import Flask
from flask_cors import CORS

from routes.share import share_routes
from routes.share_info import share_info_route
from routes.share_category import share_category_route
from routes.share_price_over_time import share_price_routes

app = Flask(__name__)
CORS(app)

app.register_blueprint(share_info_route)
app.register_blueprint(share_category_route)
app.register_blueprint(share_price_routes)
app.register_blueprint(share_routes)

if __name__ == "__main__":
    app.run(debug=True)