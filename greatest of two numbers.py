"""
A Python program that finds the greatest of two numbers inputed by user
Author - Pranav S Nair
Date - 15/10/2024
"""

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

if(num1>num2):
    print(num1 ,"is greater than", num2)
elif(num2>num1):
    print(num2 ,"is greater than", num1)
else:
    print(num1," and ",num2,"are equal")
