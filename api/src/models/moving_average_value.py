from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Date
from sqlalchemy.orm import relationship

from .base_model import Base

class Moving_Average_Value(Base):
    __tablename__ = 'moving_average_value'

    id = Column(Integer, primary_key=True)
    value = Column(Numeric(precision = 10,scale = 4, asdecimal=True), nullable = False)

    share_symbol = Column(String(20), ForeignKey("share.symbol"), nullable = False) 
    moving_average_category_id = Column(Integer, ForeignKey("moving_average_category.id") )
    recorded_date = Column(Date, nullable = False)

    share = relationship("Share", back_populates = "moving_average_values")
    moving_average_category = relationship("Moving_Average_Category", back_populates = "moving_average_values")
    