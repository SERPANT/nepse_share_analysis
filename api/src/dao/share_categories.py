from db import db
from models.share_categories import Share_Category
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
        return session.query(Share_Category).options(joinedload(Share_Category.share)).all()
    except Exception:
        print('Fetching share category failed')