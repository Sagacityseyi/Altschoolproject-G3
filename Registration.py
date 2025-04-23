from fastapi import FastAPI, status, HTTPException, File, UploadFile, Form
from pydantic import BaseModel
from typing import List, Dict, Optional, Annotated

app = FastAPI()


#Data model to register the student information
class student (BaseModel):
      name: str
      email: str
    
    #Data model to register the teacher information  
class teacher (BaseModel):
      name: str
      email: str
    
    #Data model to sumbit and extract assignment from the student  
class Assignment (BaseModel):
      id: int
      student_name: str
      subject: str
      description: str
      filename: str
      comments: List[str] = []
      
      #POST methode to register a student
      @app.post("/students", status_code=status.HTTP_201_CREATED)
      def register_student(user: student):
            return {"Message": "Registration completed!", "data": user}
      
      #POST methode to register a teacher
      @app.post("/teachers", status_code=status.HTTP_201_CREATED)
      def register_teacher(user: teacher):
            return {"Message" : "Registration completed", "data": user}
      
      
      @app.post("/Assignments")
      async def submit_assignment(
            student_name: Annotated [str, Form()],
            subject: Annotated[str, Form()],
            description: Annotated [str, Form()],
            file: Annotated [UploadFile, File()]
            ):
                        return {"Message": "Assignment submitted successfully"}