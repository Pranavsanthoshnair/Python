"""
A program that uses functions from the math module of python
Author - Pranav S Nair
Date - 05/10/2024
"""

number = int(input("Enter the number : "))
import math
square_root = math.sqrt(number)
factorial = math.factorial(number)
power = math.pow(number,2)
print("\n\nSquare root of",number,":",square_root,"\n\nFactorial of",number,":",factorial,'''\n\n''',number, "raised to power 2:",power)
