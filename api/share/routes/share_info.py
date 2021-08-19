from flask import Blueprint, Response, request

from constants.routes import ROUTES
from services.share_service import share_services

share_info_route = Blueprint('share_info', __name__, url_prefix=ROUTES.SHARE_INFO)

@share_info_route.route('/monthly')
def monthly_data():
    category = request.args.get('category')

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  share_services.fetch_monthly_data(category)
    return response


@share_info_route.route('/daily')
def daily_data():
    category = request.args.get('category')

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  share_services.fetch_daily_data(category)
    return response


@share_info_route.route('/weekly')
def weekly_data():
    category = request.args.get('category')

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  share_services.fetch_weekly_data(category)
    return response


@share_info_route.route('/quaterly')
def quaterly_data():
    category = request.args.get('category')

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  share_services.fetch_quaterly_data(category)
    return response


@share_info_route.route('/yearly')
def yearly_data():
    category = request.args.get('category')

    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  share_services.fetch_yearly_data(category)
    return response