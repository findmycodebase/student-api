from fastapi import FastAPI

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

@app.get("/student/{name}")
def get_student(name: str):
    return {
        "message": f"Welcome, {name}!"
    }

@app.get("/student/{name}/{age}")
def get_student_info(name: str, age: int):
    return {
        "message": f"Student Name: {name}, Age: {age}"
    }