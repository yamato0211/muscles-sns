from email.policy import default
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from uuid import uuid4

Base = declarative_base()

def create_uuid():
    return str(uuid4())

class User(Base):
    __tablename__ = "users"
    user_id = Column(String,primary_key=True, default=create_uuid)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String, nullable=True)