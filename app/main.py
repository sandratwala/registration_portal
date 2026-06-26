from fastapi import FastAPI
from pydantic import BaseModel
from database import (create_table, add_students, get_students, add_teachers, get_teachers, add_courses, get_courses)

app = FastAPI()
@app.get("/")
def home():
    return{"message":"welcome to my API server"}
@app.get("/students")

def list_students():
    students = get_students()
    return students

class Student(BaseModel):
    name:str
    age:int
    email:str
    country:str
    id_number:int
@app.post("/students")
def register_student(student: Student):
    add_students(student.name, student.age, student.email, student.country, student.id_number)

    return{"message":"student registered","student":student}

@app.get("students|{id}")
def student_detail(id:int):
    student = get_students(id)
    return student

@app.put("/students/{id}")
def update_teacher (id:int, student:Student):
    update_teacher(student.name, student.email, student.department, student.salary, student.id_number)
    return{"message":"student updated", "student": student}

@app.delete("/students/{id}")
def delete_student(id:int):
    delete_student(id)
    return {"message": "student details deleted"}

class Teacher(BaseModel):
    name:str
    email: str
    salary: float
    department: str
    idnumber:int

@app.post("/teachers")
def register_teacher(teacher: Teacher):
    add_teachers(teacher.name, teacher.email, teacher.salary, teacher.department, teacher.id_number)

    return{"message":"teacher registered","teacher":teacher}

@app.get("teachers|{id}")
def teacher_detail(id:int):
    teacher = get_teachers(id)
    return teacher

@app.put("/teachers/{id}")
def update_teacher (id:int, teacher:Teacher):
    update_teacher(teacher.name, teacher.email, teacher.department, teacher.salary, teacher.id_number)
    return{"message":"teacher updated", "teacher": teacher}

@app.delete("/teachers/{id}")
def delete_teacher(id:int):
    delete_teacher(id)
    return {"message": "teacher details deleted"}



class Course(BaseModel):
    name:str
    code: str
    semester: float
    department: str
    credits:int

@app.post("/courses")
def register_teacher(course: Course):
    add_teachers(course.name, course.code, course.semester, course.department, course.credit)

    return{"message":"course registered","course":course}

@app.get("course|{id}")
def course_detail(id:int):
    course = get_courses(id)
    return course

@app.put("/course/{id}")
def update_course (id:int, course:Course):
    update_course(id, course.name, course.code, course.semester, course.department, course.credit)
    return{"message":"course updated", "teacher": course}

@app.delete("/course/{id}")
def delete_course(id:int):
    delete_course(id)
    return {"message": "course details deleted"}


