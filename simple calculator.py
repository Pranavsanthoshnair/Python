"""
 A Python program of a Simple desktop calculator using Python. Only the five basic arithmetic operators.
Author - Pranav S Nair
Date - 08/10/2024
"""

num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2
result = (num1 + num2) * num3/ 2

print("The sum of ",num1," and ",num2," is: ",addition)
print("The difference when ",num2,"is subtracted from ",num1,"is: ",subtraction )
print("The product of", num1," and ",num2,"is: ",multiplication)
print("The quotient when ",num1,"is divided by ",num2, "is: ",division)
print("The remainder when ",num1,"is divided by ",num2 ,"is: ",modulus)
print("The result of (num1 + num2) * num3 / 2 is: ",result)


