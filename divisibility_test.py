"""
Pranav S Nair
15/10/2024
A Python program that checks the divisibility of a number entered by the user by another number entered by the user
"""


num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

divisibility = num1 % num2

if(divisibility == 0):
    print("The number",num1,"is divisible by number",num2)
else:
    print("The number",num1,"is not divisible by number",num2)
