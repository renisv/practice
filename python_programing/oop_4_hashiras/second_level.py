from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    

class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height




class Student:
    school_name = "Default School" 
    
    def __init__(self, name):
        self.name = name
        self.grades = []
    
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name
    
    @staticmethod
    def calculate_average(grades):
        if not grades:
            return 0
        return sum(grades) / len(grades)
    
    def calculate_avg(self):
        return Student.calculate_average(self.grades)
