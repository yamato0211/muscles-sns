import os
from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Dockerのdb設定
DATABASE = "postgresql"
USER = os.environ.get("POSTGRES_USER")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
HOST = os.environ.get("POSTGRES_HOST")
NAME = os.environ.get("POSTGRES_NAME")
SQLALCHEMY_DATABASE_URL = "{}://{}:{}@{}/{}".format(
    DATABASE, USER, PASSWORD, HOST, NAME
)

#herokuのdb設定
#SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL').replace('postgres://', 'postgresql://', 1)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    try:
        db_session = SessionLocal()
        yield db_session
    finally:
        db_session.close()
