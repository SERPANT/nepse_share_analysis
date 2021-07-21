from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base_model import Base

class Share_Category(Base):
    __tablename__ = 'share_category'

    name = Column(String(50), nullable = False)
    id = Column(Integer, primary_key = True, autoincrement = True)

    share = relationship("Share", back_populates = "share_category")
