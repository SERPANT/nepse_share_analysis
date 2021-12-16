from share.db import db

from share.models.share import Share
from share.models.moving_average_value import Moving_Average_Value
from share.models.share_basic_info import Share_Basic_Info
from share.models.share_categories import Share_Category
from share.models.moving_average_category import Moving_Average_Category
from share.models.share_price import Share_Price

def migrate():
    db.sync_database()
    