from fastapi import FastAPI, status, HTTPException, File, UploadFile, Form
from fastapi.responses import FileResponse
from typing import List, Dict, Optional, Annotated
import uuid
from uuid import UUID
import os


app = FastAPI()




#student, teacher and assignment database
students : list[student] = []
teachers : list[teacher] = []
assignments : dict[Assignment] = {}
      
#POST method to register a student
@app.post("/students", status_code=status.HTTP_201_CREATED)
def register_student(user: student):
      create_student = user.model_dump()
      students.append(create_student)
      return {"Message": "Registration completed!", "data": create_student}
      
#POST method to register a teacher
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
      file: UploadFile = File(...)
      ):


      # check if student is registered
      if not any(s["name"] == name for s in students):
         raise HTTPException(status_code=404, detail="Student not registered")
   

      
      # Generate unique assignment ID
      assignment_id = str(uuid.uuid4())
      # Check if the file is empty
      if file.filename == "":
            raise HTTPException(status_code=400, detail="File is empty")
      # Check if the file size exceeds 20 MB
      if file.file._file.tell() > 20 * 1024 * 1024:
            raise HTTPException(status_code=400, detail="File size exceeds 10 MB")

      # Create unique filename
      filename = f"{name}-{uuid.uuid4()}-{file.filename}"
      file_path = f"assignments/{filename}"
      os.makedirs("assignments", exist_ok=True)

      with open(file_path, "wb") as f:
            f.write(await file.read())

      # Create and store the assignment data
      assignment_data = Assignment(
            id=assignment_id,
            student_name=name,
            subject=subject,
            description=description,
            filename=filename
      )
      assignments[assignment_id] = assignment_data
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

# Get assignments for a specific student
@app.get("/studentslist/{name}/assignmentlist", status_code=status.HTTP_200_OK)
def get_student_assignments_by_name(name: str):
    student_assignments = [
        assignment for assignment in assignments.values()
        if assignment.student_name == name
    ]

    if not student_assignments:
        raise HTTPException(status_code=404, detail="No assignments found for this student")

    return student_assignments

# Get a single assignment record by ID
@app.get("/assignments/{assignment_id}", status_code=status.HTTP_200_OK)
def get_assignment_by_id(assignment_id: str):
    assignment = assignments.get(assignment_id)
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    return assignment

# Teacher downloads assignment file by ID
@app.get("/assignments/{assignment_id}/file", status_code=status.HTTP_200_OK)
def download_assignment_file(assignment_id: str):
    assignment = assignments.get(assignment_id)
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")

    file_path = f"assignments/{assignment.filename}"
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(path=file_path, filename=assignment.filename, media_type='application/octet-stream') #download regardless of file type

# Teacher adds a comment to an assignment
@app.put("/assignments/{assignment_id}/comment" , status_code=status.HTTP_201_CREATED)
def add_teacher_comment (assignment_id: str, comment: str):
      assignment = assignments.get(assignment_id)
      if not assignment:
            raise HTTPException(status_code=404,detail ="Assignment not found")
      assignment.teacher_comment = comment
      return{"message":"comment added successfully" , "assignment": assignment.dict()}

