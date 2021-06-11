from src.db import db

from src.models.share import Share
from src.models.moving_average_value import Moving_Average_Value
from src.models.share_basic_info import Share_Basic_Info
from src.models.share_categories import Share_Category

def migrate():
    db.sync_database()
    