from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.orm import relationship

from .base_model import Base

class Moving_Average_Category(Base):
    __tablename__ = 'moving_average_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable = False)

    moving_average_values = relationship("Moving_Average_Value", back_populates = "moving_average_category")
