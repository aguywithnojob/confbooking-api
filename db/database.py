from typing import final
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

SQL_DB_URL = "sqlite:///./bookingapp.ab"

engine = create_engine(SQL_DB_URL, connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()