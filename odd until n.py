"""
Pranav S Nair
15/10/2024
A Python program that outputs odd numbers until n(given by the user)

"""

limit = int(input("Enter the limit : "))
odd_number = 1
while odd_number <= limit:
    print(odd_number,"\t",end="")
    odd_number += 2