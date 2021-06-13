from db import db

from models.share_price import Share_Price

def fetch_range_by_share(start_date, end_date, share_symbol):
    session = db.create_session()

    lower_share_symbol = share_symbol.lower()
    start_date_str = start_date.strftime("%Y-%m-%d %H:%M:%S")
    end_date_str = end_date.strftime("%Y-%m-%d %H:%M:%S")

    return session.query(Share_Price)\
    .filter(Share_Price.share_symbol == lower_share_symbol, 
    Share_Price.date_time >= start_date_str, 
    Share_Price.date_time <= end_date_str)\
    .all()


def create(share_price_obj):
    session = db.create_session()

    try:
        session.add(share_price_obj)
        session.commit()
    except:
        raise
        print('creating share price object failed')

