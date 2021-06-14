from db import db
from models.moving_average_value import Moving_Average_Value

from sqlalchemy.sql import func

def create(moving_average_value_obj): 
    session = db.create_session()

    try:
        session.add(moving_average_value_obj)
        session.commit()
    except:
        print("Creating moving average failed")


def get_all_latest_for_all_share():
    session = db.create_session()

    try: 
        sub = session.query(func.max(Moving_Average_Value.id)).group_by(Moving_Average_Value.share_symbol, Moving_Average_Value.moving_average_category_id).subquery()

        return session.query(Moving_Average_Value).filter(Moving_Average_Value.id.in_(sub)).all()
        
    except:
        raise
