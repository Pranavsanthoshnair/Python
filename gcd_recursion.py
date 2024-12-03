"""
Author - Pranav S Nair
Date - 3/12/2024
a python program to calculate greatest common divisor [GCD] of 2 numberS using recursion
"""

def gcd(n1,n2):
    if n1%n2 == 0:
        return n2
    else:
        gcd(n2,n1%n2)
        return gcd(n2,n1%n2)
x = gcd(1220,516)
print(x)