from flask import Blueprint, Response

from constants.routes import ROUTES

share_price_routes = Blueprint('share_price', __name__, ROUTES.SHARE_PRICE )

@share_price_routes('/d')
def get_daily_data():
    pass

@share_price_routes('/w')
def get_weekly_data():
    pass

@share_price_routes('/m')
def get_monthly_data():
    pass

@share_price_routes('/q')
def get_quaterly_data():
    pass

@share_price_routes('/y')
def get_yearly_data():
    pass
