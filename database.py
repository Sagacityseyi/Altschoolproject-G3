from fastapi import Depends
from typing import Annotated
import uuid
from sqlalchemy import create_engine, Column, DateTime, Text, Boolean, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.dialects.postgresql import UUID, VARCHAR

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

#create data models

class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid= True), primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR(50), nullable= False)
    email = Column(VARCHAR(), nullable= False, unique=True)


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(UUID(as_uuid= True), primary_key=True, default=uuid.uuid4)
    name = Column(VARCHAR(50), nullable= False)
    email = Column(VARCHAR(), nullable= False, unique=True)

class TeacherComment(Base):
    __tablename__ = "teacher_comments"

    id = Column(UUID(as_uuid= True), primary_key=True, default=uuid.uuid4)
    teacher_id= Column(UUID(as_uuid= True), ForeignKey("teachers.id", ondelete="CASCADE", onupdate="CASCADE"))
    comment= Column(VARCHAR(250), nullable= False)

class Assignment(Base):
    __tablename__ = "assignments"

    id= Column(UUID(as_uuid= True), primary_key=True, default=uuid.uuid4)
    student_id= Column(UUID(as_uuid= True), ForeignKey("students.id", ondelete="CASCADE", onupdate="CASCADE"))
    subject= Column(VARCHAR(25), nullable=False)
    description = Column(VARCHAR(150), nullable=True)
    filename= Column(VARCHAR(100), nullable= True)
    teacher_comment_id= Column(UUID(as_uuid= True), ForeignKey("teacher_comments.id", ondelete="CASCADE", onupdate="CASCADE"))


