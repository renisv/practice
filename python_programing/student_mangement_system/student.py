class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__grades = []

    def add_grades(self, grade):
        if type(grade) is not int:
            raise TypeError("Grade need to be an int")
        if grade < 4 or grade > 10:
            raise ValueError("Grade needs to be between 4 and 10")
        self.grades.append(grade)
    
    def calculate_average(self):
        if not self.grades:
            raise ValueError("There are no grades to calculate average")
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        avg = self.calculate_average()
        grades_str = ', '.join(str(grade) for grade in self.grades)
        return f"ID: {self.id}, Name: {self.name}, Grades: [{grades_str}], Average: {avg:.2f}"