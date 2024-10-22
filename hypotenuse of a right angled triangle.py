"""
Pranav S Nair
22/10/2024
A python program that calculates the hypotenuse of a right angled triangle according to the inputted values of height and altitude by user.
"""
import math
base = float(input("Enter the base of the right angled triangle : "))
alt = float(input("Enter the altitude of the right angled triangle : "))

hyp = math.sqrt(base**2 + alt**2)
print(hyp)