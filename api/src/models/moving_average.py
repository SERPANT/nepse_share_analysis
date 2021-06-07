from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from .base_model import Base

class Moving_Average(Base):
    __tablename__ = 'moving_average'

    id = Column(Integer, primary_key=True)
    value = Column(Numeric(precision = 2, asdecimal=True), nullable = False)

    share_symbol = Column(String(10), ForeignKey("share.symbol"), nullable = False) 

    share = relationship("share", back_populates = "moving_averages")
