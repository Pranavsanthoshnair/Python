"""
Author - Pranav S Nair
Date - 30/11/2024
a python to program to check if a triangle is right angled or not
"""

side1 = int(input("Enter length of first side : "))
side2 = int(input("Enter length of second side : "))
side3 = int(input("Enter length of first side : "))
def check_triangle():

    if ((side1**2 == side2**2 + side3**2) or
        (side2**2 == side1**2 + side3**2) or
        (side3**2 == side1**2 + side2**2)):
        print("The Triangle is a right angled triangle ")
    else:
        print("The Triangle is not a right angled triangle ")

check_triangle()
