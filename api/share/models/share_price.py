from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey

from .base_model import Base

class Share_Price(Base):
    __tablename__ = 'share_price'

    id = Column(Integer, primary_key=True)
    price = Column(Numeric(precision = 10, scale = 4, asdecimal=True), nullable = False)
    date_time = Column(DateTime(timezone = False), nullable = False)

    share_symbol = Column(String(10), ForeignKey('share.symbol'), nullable = False)

    share = relationship("Share", back_populates = "share_prices")
