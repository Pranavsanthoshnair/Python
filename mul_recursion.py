"""
Author - Pranav S Nair
Date - 3/12/2024
a python program to calculate product of 2 numbers using recursion
"""

def mul_numbers(n1,n2):
    if n2 == 1:
        return n1
    else:
        n1+mul_numbers(n1,n2-1)
        return n1+mul_numbers(n1,n2-1)

x = mul_numbers(3,5)
print(x)