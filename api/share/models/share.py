from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base_model import Base

class Share(Base):
    __tablename__ = 'share'

    name = Column(String(150), nullable = False)
    symbol = Column(String(10), primary_key = True,  unique=True, nullable = False)
    share_number_nepse = Column(Integer)

    share_category_id = Column(Integer, ForeignKey('share_category.id'), nullable = False)  

    share_basic_info = relationship("Share_Basic_Info", back_populates="share")
    share_category = relationship("Share_Category", back_populates="share")  
    moving_average_values = relationship("Moving_Average_Value", back_populates = "share")
    share_prices = relationship("Share_Price", back_populates = "share")
