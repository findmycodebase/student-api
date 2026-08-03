from fastapi import FastAPI, HTTPException

from schemas import Student
from storage import read_students, write_students

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to the Student Management API!"
    }

@app.get("/about")
def about():
    return {
        "project": "Student Management API",
        "author": "Rejoice Oyebode",
        "version": "1.0"
    }
@app.post("/students")
def create_student(student: Student):
    students = read_students()
    for existing_student in students:
        if existing_student["student_id"] == student.student_id: 
            raise HTTPException(status_code=409, detail="Student with this ID already exists.")
        elif existing_student["email"] == student.email:
            raise HTTPException(status_code=409, detail="Student with this email already exists.")
    students.append(student.model_dump())
    write_students(students)
    return {
        "message": "Student created successfully.",
        "student": student
    }

@app.get("/students")
def get_students():
    students = read_students()
    return students

@app.get("/students/{student_id}")
def get_student(student_id: str):
    students = read_students()
    for existing_student in students:
        if existing_student["student_id"] == student_id:
            return existing_student
    raise HTTPException(status_code=404, detail="Student not found.")