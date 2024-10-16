"""
A Python program that prints odd numbers upto n(specified by user
Author - Pranav S Nair
Date - 15/10/2024
"""

limit = int(input("Enter the limit : "))
odd_number = 1
count = 0
while count<limit:
    print(odd_number,"\t",end="")
    count += 1
    odd_number += 2
