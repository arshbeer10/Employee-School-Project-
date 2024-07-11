import pickle

# Employee class to hold employee details
class Employee:
    def __init__(self, emp_id, name, age, position, salary, department):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.department = department

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary}, Department: {self.department}")

# Function to add an employee
def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    position = input("Enter Employee Position: ")
    salary = float(input("Enter Employee Salary: "))
    department = input("Enter Employee Department: ")
    employee = Employee(emp_id, name, age, position, salary, department)
    employees.append(employee)
    print("Employee added successfully!")

# Function to display all employees
def display_all_employees(employees):
    if not employees:
        print("No employee records available.")
    else:
        for emp in employees:
            emp.display()

# Function to search for an employee by ID
def search_employee_by_id(employees, emp_id):
    for emp in employees:
        if emp.emp_id == emp_id:
            return emp
    return None

# Function to search employees by salary range
def search_employee_by_salary(employees, min_salary, max_salary):
    found = [emp for emp in employees if min_salary <= emp.salary <= max_salary]
    return found

# Function to search employees by age range
def search_employee_by_age(employees, min_age, max_age):
    found = [emp for emp in employees if min_age <= emp.age <= max_age]
    return found

# Function to search employees by department
def search_employee_by_department(employees, department):
    found = [emp for emp in employees if emp.department.lower() == department.lower()]
    return found

# Function to save employees to a file
def save_employees(employees, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employees, file)
    print("Employee records saved successfully!")

# Function to load employees from a file
def load_employees(filename):
    try:
        with open(filename, 'rb') as file:
            employees = pickle.load(file)
            return employees
    except FileNotFoundError:
        return []

# Main function
def main():
    filename = "employees.dat"
    employees = load_employees(filename)
    
    while True:
        print("\n--- Employee Record Keeping System ---")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Search Employee by ID")
        print("4. Search Employees by Salary Range")
        print("5. Search Employees by Age Range")
        print("6. Search Employees by Department")
        print("7. Save and Exit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if choice == 1:
            add_employee(employees)
        elif choice == 2:
            display_all_employees(employees)
        elif choice == 3:
            emp_id = input("Enter Employee ID to search: ")
            emp = search_employee_by_id(employees, emp_id)
            if emp:
                emp.display()
            else:
                print("Employee not found!")
        elif choice == 4:
            try:
                min_salary = float(input("Enter minimum salary: "))
                max_salary = float(input("Enter maximum salary: "))
            except ValueError:
                print("Invalid input! Please enter numeric values for salary.")
                continue
            found_employees = search_employee_by_salary(employees, min_salary, max_salary)
            if found_employees:
                for emp in found_employees:
                    emp.display()
            else:
                print("No employees found in the given salary range.")
        elif choice == 5:
            try:
                min_age = int(input("Enter minimum age: "))
                max_age = int(input("Enter maximum age: "))
            except ValueError:
                print("Invalid input! Please enter numeric values for age.")
                continue
            found_employees = search_employee_by_age(employees, min_age, max_age)
            if found_employees:
                for emp in found_employees:
                    emp.display()
            else:
                print("No employees found in the given age range.")
        elif choice == 6:
            department = input("Enter department to search: ")
            found_employees = search_employee_by_department(employees, department)
            if found_employees:
                for emp in found_employees:
                    emp.display()
            else:
                print("No employees found in the given department.")
        elif choice == 7:
            save_employees(employees, filename)
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()