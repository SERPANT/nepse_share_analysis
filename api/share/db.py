import sqlalchemy
from sqlalchemy.orm import sessionmaker

from config import CONFIG

from models.base_model import Base

class Db_Connection():

    def __init__(self):
        try:
            connection_string = f"postgresql://{CONFIG.db.DB_USER}:{CONFIG.db.DB_PASSWORD}@{CONFIG.db.DB_HOST}:{CONFIG.db.DB_PORT}/{CONFIG.db.DB_NAME}"

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
