from student import Student

def display_student(student):
    grades = student.grades
    grades_str = ', '.join(str(grade) for grade in grades)
    avg = student.calculate_average()
    
    print(f"ID: {student.id}  Name: {student.name}")
    print(f"Grades: {grades_str}  Average: {avg:.2f}")

def display_all_students(students):
    print("\n=== ALL STUDENTS ===")
    for student in students:
        display_student(student)
        print("─" * 40)

def display_class_statistics(students):
    total_grades = sum(sum(student.grades) for student in students)
    grade_count = sum(len(student.grades) for student in students)
    class_average = total_grades / grade_count
    
    print("\n=== CLASS STATISTICS ===")
    print(f"Total students: {len(students)}")
    print(f"Class average: {class_average:.2f}")