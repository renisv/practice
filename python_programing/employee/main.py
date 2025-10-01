from employee import Employee
from employee_repository import EmployeeRepository

if __name__ == "__main__":
    first_employee = Employee(0, "Renis", "Software Tester", 1500)
    repo = EmployeeRepository("employee.txt")

    all_employees = repo.read_employees()
    repo.write_employees(all_employees, "output.txt")
    