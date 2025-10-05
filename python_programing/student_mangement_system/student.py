class Student:
    number_of_objects = 0

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.__grades = []
        Student.number_of_objects += 1

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def grades(self):
        return self.__grades

    @id.setter
    def id(self, value):
        if type(value) is not int:
            raise TypeError("Student ID must be an integer")
        if value <= 0:
            raise ValueError("Student ID must be a positive number")
        self.__id = value

    @name.setter
    def name(self, value):
        if type(value) is not str:
            raise TypeError("Student name must be a string")
        if len(value) == 0:
            raise ValueError("Student name cannot be empty")
        self.__name = value
    
    def calculate_average(self):
        if not self.__grades:
            return 0.0
        return sum(self.__grades) / len(self.__grades)

    @classmethod
    def object_count(cls):
        return cls.number_of_objects

    def __str__(self):
        return f"Student ID: {self.id}, Name: {self.name}"

    def __dict__(self):
        return {
            "ID": self.id,
            "Name": self.name,
            "Grades": self.grades,
            "Average": f"{self.calculate_average():.2f}" if self.grades else "No grades"
        }

    def to_csv_row(self):
        """Convert student data to CSV format"""
        grades_str = ','.join(str(grade) for grade in self.grades)
        return f"{self.id},{self.name},{grades_str}"