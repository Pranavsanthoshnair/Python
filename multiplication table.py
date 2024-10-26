"""
Author - Pranav S Nair
Date - 26/10/2024
A python program to find the multiplication table of a number inputted by user
"""

num = int(input("Enter a number : "))

multiplier = 1
while multiplier<=10:
   product = multiplier*num
   print(multiplier, "*", num, "=", product)
   multiplier+=1
   


