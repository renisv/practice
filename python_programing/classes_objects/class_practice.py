class Student:
    """this class defines a student"""
    def __init__(self, name, grade, age):
        self.__name = name
        self.__grade = grade
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        self.__grade = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.__age = value

    def get_student_info(self):
        print(f"MY name is {self.name}, I am {self.age} years old.")

    def is_a_teenager(self):
        if 12 < self.age < 20:
            return f"{self.name} is a teenager"
        return f"{self.name} is not a teenager"
    
    def can_vote(self):
        return self.age >= 18

    def next_grade(self):
        return self.grade + 1

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    

if __name__ == "__main__":
    first_student = Student("Renis", 12, 22)
    second_student = Student("Sokol", 12, 28)

    print(first_student)
    first_student.get_student_info()
    print(first_student.is_a_teenager())
    print(first_student.can_vote())
    print(first_student.next_grade())
    print(first_student)