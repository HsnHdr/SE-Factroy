import datetime

class EmployeeDataBaseSystem:
    def __init__(self,file_name):
        self.file_name = file_name
        self.employee_data = self.load_employee_data(self.file_name)
        

    def load_employee_data(self,file_name)->dict:
        employee_data = {}
        with open(file_name, 'r') as file:
            for line in file:
                emp_id, username, timestamp, gender, salary = line.strip().split(', ')
                employee_data[emp_id] = {
                   'username': username,
                    'timestamp': timestamp,
                    'gender': gender,
                    'salary': int(salary)
                }
        return employee_data
    
    def display_statistics(self):
        male_count = sum(1 for emp_info in self.employee_data.values() if emp_info['gender'] == 'male')
        female_count = len(self.employee_data) - male_count
        print(f"Male employees: {male_count}, Female employees: {female_count}")

    def add_employee(self):
        emp_id = f"emp{str(len(self.employee_data) + 1).zfill(3)}"
        username = input("Enter username: ")
        gender = input("Enter gender (male/female): ")
        salary = int(input("Enter salary: ")) 
        self.employee_data[emp_id] = {
        'username': username,
        'timestamp': datetime.datetime.now().strftime('%Y%m%d'),
        'gender': gender,
        'salary': salary
        }

    def display_employees(self):
        sorted_employees = sorted(self.employee_data.items(), key=lambda x: x[1]['timestamp'], reverse=True)
        for emp_id, emp_info in sorted_employees:
            print(f"ID: {emp_id}, Username: {emp_info['username']}, Gender: {emp_info['gender']}, Salary: {emp_info['salary']}")


    def change_salary(self):
        emp_id = input("Enter employee ID: ")
        if emp_id in self.employee_data:
            new_salary = int(input("Enter new salary: "))
            self.employee_data[emp_id]['salary'] = new_salary
            print("Salary updated successfully.")
        else:
            print("Employee not found.")

    def remove_employee(self):
        emp_id = input("Enter employee ID to remove: ")
        if emp_id in self.employee_data:
            del self.employee_data[emp_id]
            print("Employee removed successfully.")
        else:
            print("Employee not found.")
    
    def raise_salary(self):
        emp_id = input("Enter employee ID: ")
        if emp_id in self.employee_data:
            raise_percentage = float(input("Enter raise percentage: "))
            self.employee_data[emp_id]['salary'] *= raise_percentage
            print("Salary raised successfully.")
        else:
            print("Employee not found.")

    def save_employee_data(self):
        with open(self.file_name, 'w') as file:
            for emp_id, emp_info in self.employee_data.items():
                file.write(f"{emp_id}, {emp_info['username']}, {emp_info['timestamp']}, {emp_info['gender']}, {emp_info['salary']}\n")

    def adminSelection(self,selected_choice):
        if selected_choice == '1':  
            return self.display_statistics()
        elif selected_choice == '2':
            return self.add_employee()
        elif selected_choice == '3':
            return self.display_employees()
        elif selected_choice == '4':
            return self.change_salary()
        elif selected_choice == '5':
            return self.remove_employee()
        elif selected_choice == '6':
            return self.raise_salary()
        elif selected_choice == '7':
            return self.save_employee_data('employee_data.txt')
            # break
        else:
            print("Invalid choice. Please try again.")


    def run(self):
        print(self.employee_data)
        user_name = input('Enter username: ')
        password = input('Enter password: ')
        if user_name == "admin" and password == "admin123123":
            print("""
            Admin Menu:
            1. Display Statistics
            2. Add an Employee
            3. Display all Employees
            4. Change Employee's Salary
            5. Remove Employee
            6. Raise Employee's Salary
            7. Exit
            """)
            selected_choice = input("Enter your choice: ")
            self.adminSelection(selected_choice)
        elif user_name in self.employee_data and password == "":
            emp_info = self.employee_data[user_name]
            salutation = "Mr." if emp_info['gender'] == 'male' else "Ms."
            print(f"Hi {salutation} {emp_info['username']}")
            print("""
            Employee Menu:
            1. Check my Salary
            2. Exit
""")
            selected_choice = input("Enter your choice: ")
            if selected_choice == '1':
                print(f"Your salary: {emp_info['salary']}")
            elif selected_choice == '2':
                with open('login_timestamps.txt', 'a') as login_file:
                    login_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    login_file.write(f"{emp_info['username']} logged in at {login_time}\n")
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Incorrect Username and/or Password.")

if __name__ == "__main__":
    EmployeeDataBaseSystem('employees.txt').run()