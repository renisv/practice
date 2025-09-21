from student import Student
from search_for_student import search_student_by_id, search_student_by_name

def add_new_student(students, student_id, name):
    if search_student_by_id(students, student_id) is not None:
        raise ValueError(f"Student with ID {student_id} already exists")
        
    if search_student_by_name(students, name) is not None:
        raise ValueError(f"Student with name '{name}' already exists")
    
    new_student = Student(student_id, name)
    students.append(new_student)
    return new_student

def delete_student_by_id(students, student_id):
    student = search_student_by_id(students, student_id)
    if student is None:
        raise ValueError(f"Student with ID {student_id} not found") 
    students.remove(student)
    return student

def delete_student_by_name(students, name):
    student = search_student_by_name(students, name)
    if student is None:
        raise ValueError(f"Student with name '{name}' not found")
    students.remove(student)
    return student