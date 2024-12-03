"""
Author - Pranav S Nair
Date - 3/12/2024
a python program to calculate factorial of a number using recursion
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
y = factorial(5)
print(y)
