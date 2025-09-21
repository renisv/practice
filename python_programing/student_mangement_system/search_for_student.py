from student import Student

def search_student_by_id(students, student_id):
    for student in students:
        if student.id == student_id:
            return student
    return None

def search_student_by_name(students, name):
    for student in students:
        if student.name == name:
            return student
    return None