class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        self.age = value
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    def print_me(self):
        print(f"Hi i am {self.name}, i am {self.age} years old and my salary is {self.salary}")


employee1 = Employee("Koli", 28, 0)
employee2 = Employee("Renis", 22, 0)
employee3 = Employee("Enea", 34, 1000)


print(employee1)