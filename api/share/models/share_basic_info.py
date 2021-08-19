from sqlalchemy import Column, Integer, String, Numeric, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from .base_model import Base

class Share_Basic_Info(Base):

    __tablename__ = "share_basic_info"

    id = Column(Integer, primary_key = True)

    # market_price = Column(Numeric(precision = 2, asdecimal=True))
    # percentage_change = Column(Float)
    
    share_outstanding = Column(String(20))
    one_year_yield = Column(String(10))
    eps = Column(String(50))
    eps_value = Column(Numeric(precision = 10,scale = 4, asdecimal=True))
    pe_ratio = Column(Float)
    book_value = Column(Numeric(precision = 10, scale = 4,asdecimal=True))
    pbv = Column(Float)
    percentage_divident = Column(String(50))
    percentage_divident_value = Column(Float)
    percentage_bonus = Column(String(50))
    percentage_bonus_value = Column(Float)
    right_share = Column(String(50))
    right_share_value  = Column(String(10))
    record_date =  Column(DateTime(timezone = False), nullable = False)

    share_symbol = Column(String(10), ForeignKey('share.symbol'), nullable = False)
    
    share = relationship("Share", back_populates="share_basic_info")
