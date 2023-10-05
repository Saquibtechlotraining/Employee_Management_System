employees_data = []  # Finally all data from dictionary stored in a list.

def Add_Employee():
    while True:
        emp_id = input("Enter the id to be checked:")
        if any(emp["ID"] == emp_id for emp in employees_data):
            print("Employee already exist:")
            continue
        else:
            break

    emp_name = input("Enter the name:").title()
    emp_age = int(input("Enter the age:"))
    emp_gender = input("Enter the gender:").title()
    emp_position = input("Enter the position:").title()
    emp_salary = int(input("Enter the salary:"))
    employee = {"ID": emp_id, "Name": emp_name, "Age": emp_age, "Gender": emp_gender, "Position": emp_position, "Salary": emp_salary}
    employees_data.append(employee)
    print("Employee added successfully")

def Update_Employee():
    print("Which Information you want to update:")
    y = """    1. Name
    2. Age
    3. Gender
    4. Position
    5. Salary"""
    print(y)

    choice = int(input("Enter your choice:"))
    for employee in employees_data:
        if choice == 1:
            Update_Name = input("Enter the Updated Name:").title()
            employee['Name'] = Update_Name
            print(f"Employee Name {Update_Name} updated successfully")

        elif choice == 2:
            Update_Age = int(input("Enter the Update Age:"))
            employee['Age'] = Update_Age
            print(f"Employee Age {Update_Age} updated successfully")

        elif choice == 3:
            Update_Gender = input("Enter the Update Gender:").title()
            employee['Gender'] = Update_Gender
            print(f"Employee Gender {Update_Gender} updated successfully")

        elif choice == 4:
            Update_Position = input("Enter the Update Position:").title()
            employee['Position'] = Update_Position
            print(f"Employee Position {Update_Position} updated successfully")

        elif choice == 5:
            Update_Salary = int(input("Enter the Update Salary:"))
            employee['Salary'] = Update_Salary
            print(f"Employee Salary {Update_Salary} updated successfully")

        else:
            pass

def Delete_Employee():
    emp_id = input("Enter the employee ID to be delete:")
    for employee in employees_data:
        if employee["ID"] == emp_id:
            emp_details_delete = employee
            employees_data.remove(emp_details_delete)
            print(f"Employee details of {emp_id} id deleted successfully")

        else:
            print(f"Employee with this Id {emp_id} doesn't exist in the employees_data")

def List_Employees():
    if len(employees_data) == 0:
        print("No employee data")
    else:
        print("{:<10} {:<20} {:<10} {:<10} {:<20} {:<10}".format("ID", "Name", "Age", "Gender", "Position", "Salary"))

        for employee in employees_data:
            print("{:<10} {:<20} {:<10} {:<10} {:<20} {:<10}".format(employee["ID"], employee["Name"], employee["Age"], employee["Gender"], employee["Position"], employee["Salary"]))

while True:
    print("...Employee Management System...")
    x = """    1. Add Employee
    2. Update Employee
    3. Delete Employee
    4. List Employees
    5. Exit"""
    print(x)
    ch = int(input("Enter your choice:"))

    if ch == 1:
        Add_Employee()

    elif ch == 2:
        Update_Employee()

    elif ch == 3:
        Delete_Employee()

    elif ch == 4:
        List_Employees()

    elif ch == 5:
        break

    else:
        print("Wrong choice")


