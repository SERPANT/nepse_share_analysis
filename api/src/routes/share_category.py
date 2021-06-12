import json
from flask import Blueprint, Response, request

from models.share_categories import Share_Category
import services.share_categories as share_categories_services

from constants.routes import ROUTES
from utils.alchemy_encoder import AlchemyEncoder

share_category_route = Blueprint('share_category', __name__, url_prefix=ROUTES.SHARE_CATEGORY)

@share_category_route.route('/', methods = ['GET'])
def fetch_all():
    data = share_categories_services.fetch_all_with_share()
    
    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = AlchemyEncoder.parse_model_to_json(data)
    
    return response

@share_category_route.route('/', methods = ['POST'])
def create():
    data = request.json
    if data == None:
        raise "No data"
    
    share_category_obj= Share_Category(name = data["name"])

    share_categories_services.create(share_category_obj)
    
    response = Response(status = 201, mimetype='application/json')

    return response
