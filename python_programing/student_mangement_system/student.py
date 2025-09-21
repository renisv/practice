class Student:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__grades = []

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_grades(self):
        return self.__grades

    def add_grade(self, grade):
        if type(grade) is not int:
            raise TypeError("Grade needs to be an int")
        if grade < 4 or grade > 10:
            raise ValueError("Grade needs to be between 4 and 10")
        self.__grades.append(grade)
    
    def calculate_average(self):
        if not self.__grades:
            raise ValueError("There are no grades to calculate average")
        return sum(self.__grades) / len(self.__grades)

    def __str__(self):
        return f"ID: {self.__id}, Name: {self.__name}"