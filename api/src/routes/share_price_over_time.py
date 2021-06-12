from datetime import datetime, timedelta
from flask import Blueprint, Response, request

from decimal import Decimal

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
    #share_symbol = request.args.get('share')
    share_symbol = "hbl"
    today = datetime.now()
    a_week_back = timedelta(days=7)

    data = share_price_over_time_services.fetch_range_by_share(today - a_week_back, today, share_symbol)

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data = AlchemyEncoder.parse_model_to_json(data)
    
    return response

@share_price_routes.route('/m')
def get_monthly_data():
    share_symbol = request.args.get('share')
    pass

@share_price_routes.route('/q')
def get_quaterly_data():
    share_symbol = request.args.get('share')
    pass

@share_price_routes.route('/y')
def get_yearly_data():
    share_symbol = request.args.get('share')
    pass

@share_price_routes.route('/', methods = ["POST"])
def insert_data():
    data = request.json

    if data == None:
        raise "No data"

    date_time = datetime.strptime(data["time"], '%Y-%m-%d %H:%M:%S')

    share_price_obj = Share_Price(price = Decimal(data["price"]), date_time = date_time, share_symbol= data["shareSymbol"])

    share_price_over_time_services.create(share_price_obj)

    return Response(status = 201, mimetype='application/json')

