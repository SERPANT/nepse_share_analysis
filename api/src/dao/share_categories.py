from db import db

from models.share import Share
from models.share_basic_info import Share_Basic_Info
from models.share_categories import Share_Category

from sqlalchemy.sql import func
from sqlalchemy.orm import joinedload

def fetch_all():
    try:
        session = db.create_session()
        return session.query(Share_Category).all()
    except Exception:
        print('Fetching share category failed')



def fetch_all_with_share():
    try:
        session = db.create_session()

        filter_share_basic = session.query(func.max(Share_Basic_Info.id)).group_by(Share_Basic_Info.share_symbol).subquery()

        return session.query(Share_Category).options(joinedload(Share_Category.share).joinedload(Share.share_basic_info.and_(Share_Basic_Info.id.in_(filter_share_basic)))).all()

    except Exception:
        raise
        print('Fetching share category failed')


def create(share_category):
    session = db.session_maker()
    try:
        session.add(share_category)
        session.commit()
    except:
        print('failed to create share category')

        