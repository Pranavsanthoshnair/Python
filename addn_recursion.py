"""
Author - Pranav S Nair
Date - 3/12/2024
a python program to calculate sum of 2 numbers using recursion
"""

def add_numbers(n1,n2):
    if n2 == 0:
        return n1
    else:
        add_numbers(n1+1,n2-1)
        return add_numbers(n1+1,n2-1)
x = add_numbers(3,4)
print(x)