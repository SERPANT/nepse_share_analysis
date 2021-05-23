from flask import Blueprint, Response

from services.commercial_bank_data import commercial_bank_services

commercial_bank_route = Blueprint('commercial_bank_route', __name__, url_prefix='/commercialBank')

@commercial_bank_route.route('/monthly')
def monthly_data():
    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  commercial_bank_services.fetch_monthly_data()
    return response


@commercial_bank_route.route('/daily')
def daily_data():
    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  commercial_bank_services.fetch_daily_data()
    return response


@commercial_bank_route.route('/weekly')
def weekly_data():
    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  commercial_bank_services.fetch_weekly_data()
    return response


@commercial_bank_route.route('/quaterly')
def quaterly_data():
    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  commercial_bank_services.fetch_quaterly_data()
    return response


@commercial_bank_route.route('/yearly')
def yearly_data():
    response = Response()
    response.headers["Content-Type"] = "application/json"
    response.data =  commercial_bank_services.fetch_yearly_data()
    return response