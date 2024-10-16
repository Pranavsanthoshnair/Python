"""
A Python program to find sum of digits of a number
Pranav S Nair
15/10/2024
"""

num = int(input("Enter number : "))
sum = 0
while(num>0):
    rem = num % 10
    num //= 10
    sum = sum + rem
print("The sum of the digits of the number is",sum)
