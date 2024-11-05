class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Payroll:
    def __init__(self, employees):
        self.employees = employees  # List of Employee objects

    def calculate_total_payroll(self):
        return sum(employee.salary for employee in self.employees)

# Create a list to store Employee instances
employees = []

# Function to add an employee
def add_employee(employees, name, salary):
    employee = Employee(name, salary)
    employees.append(employee)  # Append the Employee object to the list

# Usage
add_employee(employees, "Joseph", 1000)
add_employee(employees, "Habiba", 2000)
add_employee(employees, "Bob", 40000)

# Create a Payroll instance with the list of employees
payroll = Payroll(employees)

# Calculate total payroll
total_payroll = payroll.calculate_total_payroll()
print(f"Total Payroll: {total_payroll}")

# Print employee details
for emp in employees:
    print(f"Employee Name: {emp.name}, Salary: {emp.salary}")


 ##Represents an employee with name and salary attributes.
 ##Takes a list of Employee objects as an argument and has a method calculate_total_payroll() to sum their salaries.
 ##The add_employee function creates Employee instances and adds them to the employees list.
 ##After creating Employee instances, a Payroll instance is created to calculate and print the total payroll.