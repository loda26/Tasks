from sqlalchemy import create_engine, Column, String
from datetime import datetime
from models.base_model import BaseModel, Base




class Users(BaseModel, Base):
    __tablename__ = 'users'

    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
