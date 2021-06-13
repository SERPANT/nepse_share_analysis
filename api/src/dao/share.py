from db import db

def create(share):
    session = db.create_session()

    try: 
        session.add(share)
        session.commit()
    except:
        print("creating share failed")