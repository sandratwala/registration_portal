
import sqlite3
from contextlib import contextmanager

sqlite_file_name = "school.db"

@contextmanager
def get_connection():
    connection = sqlite3.connect(sqlite_file_name)
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    finally:
        connection.close()

def create_table():
    with get_connection() as connection:
        connection.execute('''CREATE TABLE IF NOT EXISTS students (
                           
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           age INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           country TEXT NOT NULL,
                           id_number INTEGER NOT NULL
                           )''')
        
        connection.execute('''CREATE TABLE IF NOT EXISTS teachers (
                           
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           department INTEGER NOT NULL,
                           email TEXT NOT NULL,
                           salary TEXT NOT NULL
                           id_number NOT NULL
                           )''')
        

        connection.execute('''CREATE TABLE IF NOT EXISTS courses (
                           
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT NOT NULL,
                           code INTEGER NOT NULL,
                           semester TEXT NOT NULL,
                           department TEXT NOT NULL
                           credits NOT NULL
                           )''')


def add_students(name, age, email, country, id_number):
    with get_connection() as connection:
        connection.execute(
        'INSERT INTO students (name, age, email, country, id_number) VALUES (?, ?, ?, ?, ?)',
        (name, age, email, country,  id_number),
    )

def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT *FROM students'). fetchall()
    
def get_students(student_id):
    with get_connection() as connection:
        return connection.execute('SELECT *FROM students WHERE id = ?', (student_id)). fetchone()
def update_student(student_id, name, age, email, id_number):
    with get_connection() as connection:
        connection.execute(
            '''UPDATE students
            SET name = ?, age = ?, email = ?, id_number = ?
            WHERE id = ?''',
            (name, age, email, id_number, student_id)
            )
def delete_student(student_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM students WHERE id = ?', (student_id,))






def add_teachers(name, department, email, salary, id_number):
    with get_connection as connection:
        connection.execute(
            'INSERT INTO teachers (name, department, email, salary, id_number) VALUES (?, ?, ?, ?, ?)'
            (name, department, email, salary,id_number),
        )

def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT *FROM teachers'). fetchall()
    
def get_teachers(teacher_id):
    with get_connection() as connection:
        return connection.execute('SELECT *FROM students WHERE id = ?', (teacher_id)). fetchone()
    
def update_teacher(teacher_id,name,subject,email,employee_id):
    with get_connection as connection:
        connection.execute(
            '''UPDATE teachers
            SET name= ?,subject=?, email= ?,employee_id= ?
            WHERE id= ?''',(name, subject, email, employee_id, teacher_id)
            )
def delete_teacher(teacher_id):
    with get_connection as connection:
        connection.execute('DELETE FROM teachers WHERE id = ?', (teacher_id,))





def add_courses(name, course_id, semester, department, credits):
    with get_connection as connection:
        connection.execute(
            'INSERT INTO courses (name, course_id, semester, department, credits) ) VALUES (?, ?, ?, ?, ?)'
            (name,course_id, semester, department, credits),
        )

def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT *FROM students'). fetchall()
    
def get_courses(course_id):
    with get_connection() as connection:
        return connection.execute('SELECT *FROM courses WHERE id = ?', (course_id)). fetchone()
    
def update_course(course_id,title,course_code,department,max_capacity):
    with get_connection as connection:
        connection.execute(
            '''UPDATE courses
            SET title= ?,course_code=?,department=?,max_capacity=?
            WHERE id=?'''
            (title, course_code, department, max_capacity, course_id)
            )
def delete_course(course_id):
    with get_connection  as connection:
        connection.execute('DELETE FROM courses WHERE id= ?',(course_id))