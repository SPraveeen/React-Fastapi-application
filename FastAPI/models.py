from database import Base
from sqlalchemy import Column, Integer, Float, String, Boolean

class Transaction(Base):
    __tablename__='transactions'

    id=Column(Integer)
    amount=Column(Float)
    category=Column(String)
    description=Column(String)
    is_income=Column(Boolean)
    date=Column(String)