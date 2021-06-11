from db import db
from models.share import Share
from models.share_basic_info import Share_Basic_Info
from models.share_categories import Share_Category

def fetch_all():
    try:
        session = db.create_session()
        return session.query(Share_Category).all()
    except Exception:
        print('Fetching share category failed')



def fetch_all_with_share():
    try:
        session = db.create_session()

        sub_query_join_share_share_basic_info = session.query(Share).join(Share_Basic_Info, Share.symbol == Share_Basic_Info.share_symbol).subquery()

        print('ppppppppppppp   ', sub_query_join_share_share_basic_info)

        return session.query(Share_Category).join(sub_query_join_share_share_basic_info).all()

    except Exception:
        raise
        print('Fetching share category failed')
        