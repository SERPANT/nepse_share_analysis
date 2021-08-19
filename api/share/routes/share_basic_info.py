from flask import Blueprint, Response, request

from constants.routes import ROUTES

import services.share_basic_info as share_basic_info_services

from models.share_basic_info import Share_Basic_Info

from decimal import Decimal
from datetime import datetime

share_basic_info_routes = Blueprint('share_basic_info_routes', __name__, url_prefix=ROUTES.SHARE_BASIC_INFO)

@share_basic_info_routes.route('/', methods = ["POST"])
def create():
    data = request.json

    if data == None:
        raise "No data"

    share_basic_info_obj = Share_Basic_Info(
        share_outstanding = data["share_outstanding"], 
        one_year_yield = data["one_year_yield"],
        eps = data["eps"],

        eps_value = -1 if data["eps_value"] == '' else  Decimal(data["eps_value"]),

        pe_ratio = -1 if data["pe_ratio"] == '' else data["pe_ratio"],

        book_value = -1 if data["book_value"] == '' else Decimal(data["book_value"]),
        
        pbv = -1 if data["pbv"] == '' else data["pe_ratio"],
        percentage_divident = data["percentage_divident"], 

        percentage_divident_value =  -1 if data["percentage_divident_value"] == '' else data["percentage_divident_value"], 

        percentage_bonus = data["percentage_bonus"], 

        percentage_bonus_value =  -1 if data["percentage_bonus_value"] == '' else data["percentage_bonus_value"], 

        right_share = data["right_share"], 

        right_share_value = data["right_share_value"],

        record_date =  datetime.strptime(data["record_date"], '%Y-%m-%d'),

        share_symbol = data["share_symbol"])
    
    share_basic_info_services.create(share_basic_info_obj)
    
    return Response(status = 201)