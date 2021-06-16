import json
from decimal import Decimal
from datetime import datetime, timedelta
from flask import Blueprint, Response, request


from models.share_price import Share_Price 
import services.share_price_over_time as share_price_over_time_services

from constants.routes import ROUTES

from utils.alchemy_encoder import AlchemyEncoder

share_price_routes = Blueprint('share_price', __name__, url_prefix= ROUTES.SHARE_PRICE )

@share_price_routes.route('/d')
def get_daily_data():
    pass

@share_price_routes.route('/w')
def get_weekly_data():
    share_symbol = request.args.get('shareSymbol')
    share_name = request.args.get('shareName')
    today = datetime.now()
    a_week_back = timedelta(days=7)

    data = share_price_over_time_services.fetch_range_by_share(today - a_week_back, today, share_symbol, share_name)

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = json.dumps(data)

    return response

@share_price_routes.route('/m')
def get_monthly_data():
    share_symbol = request.args.get('shareSymbol')
    share_name = request.args.get('shareName')

    today = datetime.now()
    a_week_back = timedelta(days=30)

    data = share_price_over_time_services.fetch_range_by_share(today - a_week_back, today, share_symbol, share_name)

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = json.dumps(data)

    return response

@share_price_routes.route('/q')
def get_quaterly_data():
    share_symbol = request.args.get('shareSymbol')
    share_name = request.args.get('shareName')
    today = datetime.now()
    a_week_back = timedelta(days=90)

    data = share_price_over_time_services.fetch_range_by_share(today - a_week_back, today, share_symbol, share_name)

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = json.dumps(data)

    return response

@share_price_routes.route('/y')
def get_yearly_data():
    share_symbol = request.args.get('shareSymbol')
    share_name = request.args.get('shareName')
    today = datetime.now()
    a_week_back = timedelta(days=365)

    data = share_price_over_time_services.fetch_range_by_share(today - a_week_back, today, share_symbol, share_name)

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = json.dumps(data)

    return response

@share_price_routes.route('/', methods = ["POST"])
def insert_data():
    data = request.json

    if data == None:
        raise "No data"

    share_symbol = data["symbol"]
    share_prices = data["time_list"]

    for share_price in share_prices:
        date_time = datetime.strptime(share_price["time"], '%Y-%m-%d %H:%M:%S')

        share_price_obj = Share_Price(price = Decimal(share_price["value"]), date_time = date_time, share_symbol = share_symbol)

        share_price_over_time_services.create(share_price_obj)

    return Response(status = 201, mimetype='application/json')


@share_price_routes.route('/latest', methods = ["GET"])
def fetch_latest_record():
    share_symbol = request.args.get('shareSymbol')
    record = share_price_over_time_services.fetch_latest_record(share_symbol)

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = AlchemyEncoder.parse_model_obj_to_json(record, [])

    return response
        
