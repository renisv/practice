from student import Student

class StudentManager:
    def __init__(self):
        self.__student_list = []

    @property
    def student_list(self):
        return self.__student_list

    def print_students(self):
        for student in self.student_list:
            print(student)

    def search_by_id(self, student_id):
        for i, student in enumerate(self.student_list):
            if student.id == student_id:
                return i
        return -1

    def search_by_name(self, student_name):
        for i, student in enumerate(self.student_list):
            if student.name == student_name:
                return i
        return -1
        
    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("You can only add Student objects")
        
        if self.search_by_id(student.id) != -1:
            raise ValueError(f"Student with ID {student.id} already exists")
            
        self.__student_list.append(student)

    def remove_student_by_id(self, student_id):
        position = self.search_by_id(student_id)
        if position == -1:
            raise ValueError(f"Student with ID {student_id} not found")
        self.student_list.pop(position)

    def add_grade(self, student_id, grade):
        if not isinstance(grade, int) or grade < 4 or grade > 10:
            raise ValueError("Grade must be integer between 4 and 10")
            
        position = self.search_by_id(student_id)
        if position == -1:
            raise ValueError(f"Student with ID {student_id} not found")
        
        self.student_list[position].grades.append(grade)

    def display_student_details(self, student_id):
        position = self.search_by_id(student_id)
        if position == -1:
            raise ValueError(f"Student with ID {student_id} not found")
        
        student = self.student_list[position]
        grades_str = ', '.join(str(grade) for grade in student.grades)
        print(f"ID: {student.id}  Name: {student.name}")
        print(f"Grades: {grades_str}  Average: {student.calculate_average():.2f}")

    def display_all_students(self):
        print("\n=== ALL STUDENTS ===")
        for student in self.student_list:
            self.display_student_details(student.id)
            print("─" * 40)

    def display_class_statistics(self):
        if not self.student_list:
            print("No students in the system")
            return
            
        total_grades = sum(sum(student.grades) for student in self.student_list)
        grade_count = sum(len(student.grades) for student in self.student_list)
        
        class_average = total_grades / grade_count if grade_count > 0 else 0
        
        print(f"\nTotal students: {len(self.student_list)}")
        print(f"Class average: {class_average:.2f}")

    def sort_by_name(self):
        return sorted(self.student_list, key=lambda student: student.name)

    def sort_by_average(self):
        return sorted(self.student_list, key=lambda student: student.calculate_average(), reverse=True)


    def load_from_csv(self, filename="students.csv"):
        """Load students from CSV file"""
        try:
            with open(filename, 'r') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    
                    parts = line.split(',')
                    if len(parts) >= 2:
                        student_id = int(parts[0])
                        student_name = parts[1]
                        student = Student(student_id, student_name)
                        
                        
                        for grade_str in parts[2:]:
                            if grade_str:
                                student.grades.append(int(grade_str))
                        
                        self.add_student(student)
                        
            print(f"Loaded {len(self.student_list)} students from {filename}")
            
        except FileNotFoundError:
            print(f"File {filename} not found")
        except Exception as e:
            print(f"Error loading file: {e}")

    def save_to_csv(self, filename="students.csv"):
        """Save students to CSV file"""
        try:
            with open(filename, 'w') as file:
                for student in self.student_list:
                    file.write(student.to_csv_row() + '\n')
            print(f"Saved {len(self.student_list)} students to {filename}")
        except Exception as e:
            print(f"Error saving file: {e}")