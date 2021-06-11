import json
from flask import Blueprint, Response

from constants.routes import ROUTES
import services.share_categories as share_categories_services

from utils.alchemy_encoder import AlchemyEncoder

share_category_route = Blueprint('share_category', __name__, url_prefix=ROUTES.SHARE_CATEGORY)

@share_category_route.route('/')
def fetch_all():
    data = share_categories_services.fetch_all_with_share()
    
    print("-------------------------------   ", data)
    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = AlchemyEncoder.parse_model_to_json(data)
    
    return response
