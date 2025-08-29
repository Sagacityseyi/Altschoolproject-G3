from fastapi import Depends
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

#create database connection
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost:5432/altschoolproject_g3"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency= Annotated[Session, get_db]

Base = declarative_base()


