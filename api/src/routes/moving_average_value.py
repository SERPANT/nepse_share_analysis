from decimal import Decimal
from datetime import datetime
from flask import Blueprint, Response, request

from constants.routes import ROUTES

from models.moving_average_value import Moving_Average_Value
import services.moving_average_value as moving_average_value_services

import json

moving_average_value_routes = Blueprint('moving_average_routes', __name__, url_prefix=ROUTES.MOVING_AVERAGE)

@moving_average_value_routes.route('/', methods = ["POST"])
def create():
    data = request.json

    if data == None:
        raise "No data"

    moving_average_obj = Moving_Average_Value(
        value = Decimal(data["value"]),
        recorded_date =  datetime.strptime(data["record_date"], '%Y-%m-%d'),
        moving_average_category_id = data["movingAverageCategoryId"], 
        share_symbol = data["shareSymbol"])
    
    moving_average_value_services.create(moving_average_obj)
    
    return Response(status = 201)

@moving_average_value_routes.route('/', methods = ["GET"])
def get():
    response = Response()

    response.headers["Content-Type"] = "application/json"
    response.data = json.dumps(moving_average_value_services.get_all_latest_for_all_share())

    return response
