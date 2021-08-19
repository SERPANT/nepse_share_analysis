from db import db

from models.share import Share

def create(share):
    session = db.create_session()

    try: 
        session.add(share)
        session.commit()
    except:
        print("creating share failed")


def update_share_number(symbol, share_number):
    session = db.create_session()

    try: 
        session.query(Share).filter(Share.symbol == symbol).update({"share_number_nepse": share_number})
        
        session.commit()

    except:
        raise
        print("failed to update")


def fetch_by_symbol(symbol): 
    session = db.create_session()

    return session.query(Share).filter(Share.symbol == symbol).first()


def fetch_all(): 
    session = db.create_session()

    return session.query(Share).all()

    