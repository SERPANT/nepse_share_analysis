import json
from flask import Blueprint, Response, request

from utils.alchemy_encoder import AlchemyEncoder
from models.share_categories import Share_Category
import services.share_categories as share_categories_services

from constants.routes import ROUTES

import json

share_category_route = Blueprint('share_category', __name__, url_prefix=ROUTES.SHARE_CATEGORY)

@share_category_route.route('/', methods = ['GET'])
def fetch_all():
    data = share_categories_services.fetch_all_with_share()
    
    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = json.dumps(data)
    
    return response

@share_category_route.route('/name', methods = ['GET'])
def fetch_by_name():
    name = request.args.get('name')
    category = share_categories_services.fetch_by_name(name)

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = AlchemyEncoder.parse_model_obj_to_json(category, ["share"])

    return response

@share_category_route.route('/', methods = ['POST'])
def create():
    data = request.json
    if data == None:
        raise "No data"
    
    for share_category in data: 
        share_category_obj= Share_Category(name = share_category["name"])
        share_categories_services.create(share_category_obj)
    
    response = Response(status = 201, mimetype='application/json')

    return response
