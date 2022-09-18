from datetime import datetime
from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4

Base = declarative_base()

def create_uuid():
    return str(uuid4())


class Favorites(Base):
    __tablename__ = "favorites"
    user_id = Column(String, ForeignKey("users.user_id"), primary_key=True)
    post_id = Column(String, ForeignKey("posts.post_id"), primary_key=True)


class User(Base):
    __tablename__ = "users"
    user_id = Column(String,primary_key=True, default=create_uuid)
    name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String, nullable=True)


class Post(Base):
    __tablename__ = "posts"
    post_id = Column(String, primary_key=True, default=create_uuid)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    user_id = Column(String, ForeignKey("users.user_id"))
    user = relationship("User")
    favorites = relationship("User", secondary=Favorites.__tablename__)