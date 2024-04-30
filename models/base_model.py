from sqlalchemy import Column, Integer, create_engine, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime


Base = declarative_base()

class BaseModel():
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)
