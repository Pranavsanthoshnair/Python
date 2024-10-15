"""
Pranav S Nair
15/10/2024
A Python program that determines the smallest of the entered three numbers by the user
"""


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

if(num1 < num2 and num1 < num3):
    print(num1," is the smallest")
elif(num2 < num1 and num2 < num3):
    print(num2," is the smallest")
elif(num3 < num1 and num3 < num1):
    print(num3," is the smallest")
elif(num1 == num2 and num1!=num3):
    print("number 1 and number 2 are same.")
elif(num1 == num3 and num1!=num2):
    print("number 1 and number 3 are same.")
elif(num2 == num3 and num2!=num3):
    print("number 2 and number 3 are same.")
else:
    print("number 1, number 2 and number 3 are same")


