from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    location = Column(String, nullable=False)
