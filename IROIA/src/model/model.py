from sqlalchemy import Column, Integer, String, Date
from ..data.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String, nullable=False)

class TripDetail(Base):
    __tablename__="tripdetail"
    id = Column(Integer, primary_key=True, index=True)
    trip_start = Column(Date, nullable=False)
    trip_end = Column(Date, nullable=False)
    trip_country = Column(String, nullable=False)
