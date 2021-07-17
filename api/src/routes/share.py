import json
from flask import Blueprint, request, Response

from models.share import Share
from constants.routes import ROUTES

import services.share as share_services
from utils.alchemy_encoder import AlchemyEncoder

share_routes = Blueprint("share_routes", __name__, url_prefix= ROUTES.SHARE)

@share_routes.route('/', methods = ["POST"])
def create():
    data = request.json

    if data == None:
        raise "No data"

    for share in data:
        share_obj = Share(name = share["name"], symbol = share["symbol"], share_category_id = share["shareCategoryId"], share_number_nepse = share["share_number"])
        
        share_services.create(share_obj)

    return "created"



@share_routes.route('/', methods = ["PUT"])
def update_share_number():
    data = request.json

    if data == None:
        raise "no data"

    share_services.update(data["symbol"], int(data["share_number"]))

    return "updated"


@share_routes.route('/<share_symbol>', methods = ["GET"])
def get_by_share_symbol(share_symbol):

    share_record = share_services.fetch_by_symbol(share_symbol)

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = AlchemyEncoder.parse_model_obj_to_json(share_record, 
    ["share_category_id",
     "share_basic_info", 
     "share_category", 
     "moving_average_values", 
     "share_prices"])

    return response
