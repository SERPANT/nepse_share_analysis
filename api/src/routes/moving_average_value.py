from flask import Blueprint, Response, request

from constants.routes import ROUTES

import services.moving_average_value as moving_average_value_services

from models.moving_average_value import 

from decimal import Decimal

moving_average_value_routes = Blueprint('moving_average_routes', __name__, url_prefix=ROUTES.MOVING_AVERAGE)

@moving_average_value_routes.route('/', methods = ["POST"])
def create():
    data = request.json

    if data == None:
        raise "No data"

    moving_average_obj = Moving_Average_Value(
        value = Decimal(data["value"]) , 
        moving_average_category_id = data["movingAverageCategoryId"], 
        share_symbol = data["shareSymbol"])
    
    moving_average_value_services.create(moving_average_obj)
    
    return Response(status = 201)