from db import db

def create(moving_average_value_obj): 
    session = db.create_session()

    try:
        session.add(moving_average_value_obj)
        session.commit()
    except:
        print("Creating moving average failed")
