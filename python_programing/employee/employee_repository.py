from employee import Employee

class EmployeeRepository:
    def __init__(self, filepath):
        self.filepath = filepath
    
    def read_employees(self):
        employee_list = []

        try:
            with open(self.filepath, "r", encoding="UTF-8") as file:
                next(file)
                for line in file:
                    emp = Employee.deserialize(line)
                    employee_list.append(emp)
        except FileNotFoundError:
            print(f"{self.filepath} not found")
        
        return employee_list


    def write_employees(self, employee_list, output):
        try:
            with open(output, "w", encoding="UTF-8") as file:
                file.write("ID|Name|Department|Salary")
                for employee in employee_list:
                    file.write(employee.serialize()+"\n")
                    
        except FileNotFoundError:
            print(f"{output} not found")
