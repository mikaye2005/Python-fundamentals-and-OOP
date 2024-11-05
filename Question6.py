class Employee:
    def calculate_salary(self):
        print("Calculating generic employee salary.")

class Manager(Employee):
    def calculate_salary(self):
        base_salary = 50000
        bonus = 10000
        total_salary = base_salary + bonus
        print(f"Manager's salary is: ${total_salary}")

# Demonstrate the overridden behavior
# Create an instance of Employee
generic_employee = Employee()
generic_employee.calculate_salary()  # Expected output: "Calculating generic employee salary."

# Create an instance of Manager
manager = Manager()
manager.calculate_salary()  # Expected output: "Manager's salary is: $60000"
