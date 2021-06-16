from db import db

from models.share_price import Share_Price
from utils.alchemy_encoder import AlchemyEncoder
from sqlalchemy import desc

def fetch_range_by_share(start_date, end_date, share_symbol, share_name):
    session = db.create_session()

    start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")
    end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

    data = session.query(Share_Price).filter(Share_Price.share_symbol == share_symbol.strip().upper(), Share_Price.date_time >= start_date_str, Share_Price.date_time <= end_date_str).all()
    
    modified_dic = {
        "share": share_symbol,
        "shareName": share_name,
        "timeList": AlchemyEncoder.convert_model_list_to_dic(data, [])
    }

    session.close()

    return modified_dic



def create(share_price_obj):
    session = db.create_session()

    try:
        session.add(share_price_obj)
        session.commit()
    except:
        raise
        print('creating share price object failed')


def fetch_latest_record(share_symbol):
    session = db.create_session()

    return session.query(Share_Price).filter(Share_Price.share_symbol == share_symbol).order_by(desc(Share_Price.date_time)).first()