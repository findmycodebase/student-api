from pydantic import BaseModel, Field

class Studentcreate(BaseModel):
    student_id: str
    first_name: str
    last_name: str
    email: str 
    phone_number: str 
    age: int
    gender: str
    course: str 
    level: int
    cgpa: float
    status: str

class StudentUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str 
    phone_number: str 
    age: int 
    gender: str
    course: str 
    level: int
    cgpa: float
    status: str