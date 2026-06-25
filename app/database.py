from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from database import (
    create_table,
    add_students, get_all_students, get_students_by_id, update_student, delete_student_by_id,
    add_teacher, get_all_teachers, get_teacher_by_id, update_teacher, delete_teacher_by_id,
    add_course, get_all_courses, get_course_by_id, update_course, delete_course_by_id
)

app = FastAPI()
create_table()

class StudentsSchema(BaseModel):
    name: str
    age: int
    email: str
    country: str
    id_number: int

class TeacherSchema(BaseModel):
    name: str
    course_expertise: str
    email: str
    years_of_experience: int
    teacher_id: int

class CourseSchema(BaseModel):
    title: str
    course_code: str
    ratings: float
    department: str
    max_students: int

@app.get("/")
def home():
    return {"message": "Welcome to the Student Registration portal!"}

@app.post('/students')
def register_students(student: StudentsSchema):
    add_students(
        name=student.name,
        age=student.age,
        email=student.email,
        country=student.country,
        id_number=student.id_number
    )
    return {'status': 'Success', 'message': f'Student {student.name} registered successfully!'}

@app.get('/students')
def list_students():
    students = get_all_students()
    return students

@app.get('/students/{id}')
def student_detail(id: int):
    student = get_students_by_id(id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put('/students/{id}')
def edit_student(id: int, updated_data: StudentsSchema):
    student = get_students_by_id(id)
    if student is None:
        raise HTTPException(status_code=404, detail='Student not found')

    update_student(
        student_id=id,
        name=updated_data.name,
        age=updated_data.age,
        email=updated_data.email,
        country=updated_data.country,
        id_number=updated_data.id_number
    )
    return {"status": "Success", "message": f"Student profile with ID {id} has been fully updated!"}

@app.delete('/students/{id}')
def remove_student(id: int):
    student = get_students_by_id(id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")

    delete_student_by_id(id)
    return {"status": "Success", "message": f"Student with ID {id} has been permanently deleted."}

@app.post("/teachers")
def register_teacher(teacher: TeacherSchema):
    add_teacher(teacher.name, teacher.course_expertise, teacher.email, teacher.years_of_experience, teacher.teacher_id)
    return {"status": "Success", "message": f"Teacher {teacher.name} registered!"}

@app.get("/teachers")
def list_teachers():
    return get_all_teachers()

@app.get("/teachers/{id}")
def teacher_detail(id: int):
    teacher = get_teacher_by_id(id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher

@app.put("/teachers/{id}")
def edit_teacher(id: int, updated_data: TeacherSchema):
    teacher = get_teacher_by_id(id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    update_teacher(id, updated_data.name, updated_data.course_expertise, updated_data.email, updated_data.years_of_experience, updated_data.teacher_id)
    return {"status": "Success", "message": f"Teacher ID {id} updated!"}

@app.delete("/teachers/{id}")
def remove_teacher(id: int):
    teacher = get_teacher_by_id(id)
    if teacher is None:
        raise HTTPException(status_code=404, detail="Teacher not found")
    delete_teacher_by_id(id)
    return {"status": "Success", "message": f"Teacher ID {id} deleted!"}

@app.post("/courses")
def register_course(course: CourseSchema):
    add_course(course.title, course.course_code, course.ratings, course.department, course.max_students)
    return {"status": "Success", "message": f"Course {course.title} created!"}

@app.get("/courses")
def list_courses():
    return get_all_courses()

@app.get("/courses/{id}")
def course_detail(id: int):
    course = get_course_by_id(id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put("/courses/{id}")
def edit_course(id: int, updated_data: CourseSchema):
    course = get_course_by_id(id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    update_course(id, updated_data.title, updated_data.course_code, updated_data.ratings, updated_data.department, updated_data.max_students)
    return {"status": "Success", "message": f"Course ID {id} updated!"}

@app.delete("/courses/{id}")
def remove_course(id: int):
    course = get_course_by_id(id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    delete_course_by_id(id)
    return {"status": "Success", "message": f"Course ID {id} deleted!"}