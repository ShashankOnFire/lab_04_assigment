class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def print_table(self):
        print("Employee ID  Name     Age  Salary (PM)")
        for employee in self.employees:
            print(f"{employee.emp_id}      {employee.name}   {employee.age}   {employee.salary}")

    def sort_table(self, parameter):
        if parameter == 1:
            self.employees.sort(key=lambda emp: emp.age)
        elif parameter == 2:
            self.employees.sort(key=lambda emp: emp.name)
        elif parameter == 3:
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")
            return

if __name__ == "__main__":
    employee_data = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    employee_table = EmployeeTable(employee_data)

    print("Select sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    choice = int(input("Enter your choice: "))

    employee_table.sort_table(choice)
    employee_table.print_table()
