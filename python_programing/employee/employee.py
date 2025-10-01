class Employee:
    def __init__(self, ID, name, department, salary):
        self.ID = ID
        self.name = name
        self.department = department
        self.salary = salary

    @staticmethod
    def deserialize(line):
        parts = line.strip().split("|")
        if len(parts) == 4:
            emp_id, emp_name, emp_dep, emp_salary = [part.strip() for part in parts] 
            return Employee(emp_id, emp_name, emp_dep, emp_salary)
        return None

    def serialize(self):
        return f"{self.ID}|{self.name}|{self.department}|{self.salary}"

    def __str__(self):
        return f"Employee ID:{self.ID} Name:{self.name} Department:{self.department}, salary: {self.salary}"
