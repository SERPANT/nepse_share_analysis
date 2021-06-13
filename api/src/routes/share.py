from flask import Blueprint, request

from models.share import Share
from constants.routes import ROUTES

import services.share as share_services

share_routes = Blueprint("share_routes", __name__, url_prefix= ROUTES.SHARE)

@share_routes.route('/', methods = ["POST"])
def create():
    data = request.json

    if data == None:
        raise "No data"

    for share in data:
        share_obj = Share(name = share["name"], symbol = share["symbol"], share_category_id = share["shareCategoryId"])
        
        share_services.create(share_obj)

    return "created"
