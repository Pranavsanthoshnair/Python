"""
Author - Pranav S Nair
Date - 19/11/2024
a python to program to help company to manage employee information
"""

employee_details = [
    ("David","Cyber Security",35000.00),
    ("Surya","Web Development",55000.00),
    ("Arun","Prompt Engineer",45000.00),
    ("John","Accountant",25000.00),
    ("Irfan","Machine Learning Engineer",135000.00)
]
total_expense = 0
for employee in employee_details:
    Employee_name,Department,Monthly_Salary = employee
    total_expense+=Monthly_Salary*12
    if(Monthly_Salary >= 40000):
        print(f"Employee Name:{Employee_name} has a salary above specified threshold")
print(f"Total annual payroll for all employees in the company is {total_expense}")

