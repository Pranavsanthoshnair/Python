"""
Pranav S Nair
22/10/2024
A Python program that determines the largest of the entered three numbers by the user
"""
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if(num1>num2 and num1>num3):
    print(num1," is the largest")
elif(num2>num1 and num2>num3):
    print(num2," is the largest")
elif(num3>num1 and num3>num1):
    print(num3," is the largest")