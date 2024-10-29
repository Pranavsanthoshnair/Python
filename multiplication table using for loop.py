"""
Author - Pranav S Nair
Date - 29/10/2024
A Python Program to find the multiplication table of a number inputted by the user.
"""
num = int(input("Enter a number : "))
print("THE MULTIPLICATION TABLE OF ",num,"\n")
for i in range(1,13):
    product = num*i
    print(f"{num} x {i} = {product}")