import uuid
from sqlalchemy import UUID, VARCHAR, Column, ForeignKey
from database import Base


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


