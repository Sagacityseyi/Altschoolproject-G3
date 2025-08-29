from pydantic import BaseModel, EmailStr
from typing import Optional


#Data model to register the student information
class student (BaseModel):
      name: str
      email: EmailStr
    
#Data model to register the teacher information  
class teacher (BaseModel):
      name: str
      email: EmailStr
    
#Data model to sumbit and extract assignment from the student  
class Assignment (BaseModel):
      id: str
      student_name: str
      subject: str
      description: str
      filename: str
      teacher_comment: Optional[str] = None