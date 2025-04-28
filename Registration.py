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

#student, teacher and assignment database
students : list[student] = []
teachers : list[teacher] = []
assignments : dict[Assignment] = {}
      
#POST methode to register a student
@app.post("/students", status_code=status.HTTP_201_CREATED)
def register_student(user: student):
      create_student = user.model_dump()
      students.append(create_student)
      return {"Message": "Registration completed!", "data": create_student}
      
#POST methode to register a teacher
@app.post("/teachers", status_code=status.HTTP_201_CREATED)
def register_teacher(user: teacher):
      create_teacher = user.model_dump()
      teachers.append(create_teacher)
      return {"Message" : "Registration completed", "data": create_teacher}


#POST method to submit an assignment     
@app.post("/new-assignment", status_code=status.HTTP_201_CREATED)
async def submit_assignment(
      name: Annotated[str, Form()],
      subject: Annotated[str, Form()],
      description: Annotated[str, Form()],
      file: UploadFile
      ):
      
      assignment_id = len(assignments) + 1
      file.filename = (name + str(assignment_id))
      assignment_data = {
            "id" : assignment_id ,
            "name" : name,
            "subject" : subject,
            "description" : description,
            "file name" : file.filename
            }
      assignments[assignment_data["id"]] = assignment_data
      return {"Message": "Assignment submitted successfully"}



#To get the list of students data
@app.get("/studentslist", status_code=status.HTTP_200_OK)
def get_students_list():
      return students

#To get the list of teachers data
@app.get("/teacherslist", status_code=status.HTTP_200_OK)
def get_teachers_list():
      return teachers

#To get all assignments submitted
@app.get("/assignments", status_code=status.HTTP_200_OK)
def get_submitted_assignments():
      return assignments


@app.get("/studentslist/{name}/assignmentlist", status_code=status.HTTP_200_OK)
def get_student_assignments_by_name(name: str):
      student_assignments = []
      for assignment in assignments.values():
            if assignment["name"] == name:
                  student_assignments.append(assignment)
      if not student_assignments:
            raise HTTPException(status_code=404, detail="No assignments found for this student")
      return student_assignments

