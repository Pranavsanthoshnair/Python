"""
Python program that calculates the area of a circle based on the radius entered by the user
Author - Pranav S Nair
Date - 01-10-2024
"""


radius = float(input("Enter the radius of the circle : "))
pi = 22/7
area = pi * (radius**2)
print("Area of the circle with radius "+ str(radius) + " is :",area)