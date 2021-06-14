import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models.base_model import Base

class Db_Connection():

    def __init__(self):
        try:
            connection_string = 'postgresql://shreejit:root@localhost:5432/share_info'
            self.engine = sqlalchemy.create_engine(connection_string, echo=False,  pool_size=20, max_overflow=8)
            self.session_maker = sessionmaker(bind=self.engine) # used to create session
            print("Connection good")
        except: 
            print("Connection not good")

    def create_session(self):
        return self.session_maker()

    def sync_database(self):
        Base.metadata.create_all(self.engine)

db = Db_Connection()
