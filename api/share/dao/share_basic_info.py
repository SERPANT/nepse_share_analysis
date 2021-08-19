from db import db

def create(share_basic_info_obj):
    session = db.create_session()

    try:
        session.add(share_basic_info_obj)
        session.commit()
    except:
        print("basic info was not created")
