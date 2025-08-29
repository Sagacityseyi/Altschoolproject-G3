import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import TIMESTAMP, UUID, VARCHAR, Column, ForeignKey, String, func
from database import Base



class Student(Base):
    __tablename__ = "students"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    name = Column(String(100), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

    assignments = relationship("Assignment", back_populates="student", cascade="all, delete-orphan")


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


