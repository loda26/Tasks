from sqlalchemy import create_engine, Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base




class Users(BaseModel, Base):
    __tablename__ = 'users'

    name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)


engine = create_engine("sqlite:///testdb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
