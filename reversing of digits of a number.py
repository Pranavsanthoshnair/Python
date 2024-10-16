"""
A Python program that reverses the digits of inputed number
Author - Pranav S Nair
Date - 15/10/2024
"""

num = int(input("Enter any number : "))
reverse_num = 0
while(num>0):
    rem = num % 10
    reverse_num = reverse_num* 10 + rem
    num //= 10

print(reverse_num)