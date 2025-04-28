# Student Assignment Submission System 

A group backend project for students to submit assignments and also allow teachers view them as much as comment on the assignments for grading. 

## **Setup Instructions**

 1. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

 2. **Activate the virtual environment**:
    - On macOS/Linux:
        ```sh
          source .venv/bin/activate
        ```
   
    - On Windows use(Powershell):
    ```sh
      .venv/Scripts/Activate
    ```
##  **Installation** 
 1. Fork the repository and clone it:
    ```sh
    git clone https://github.com/Sagacityseyi/altschoolp.git 
    ```

 2. Navigate into project directory:
    - ```sh
    cd altschoolp
      ```

##  **Features**

1. Register student and teachers by collecting their names and email addresses
   - `def register_student(user: student):`  #for students 
   - `def register_teacher(user: teacher):`  #for teachers
 
2. Method to submit an assignment 
   - `async def submit_assignment:`

3. To get list of students and teachers data
  - `def get_students_list():`
  - `def get_teachers_list():`

4. To get all the assignments submitted 
  - `def get_submitted_assignments():`


## **Contribution Guidelines**  
- Ensure your code **follows project standards** and **passes tests** before submitting a pull request.  