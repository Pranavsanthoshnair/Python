"""
Author - Pranav S Nair
Date - 12/11/2024
A python program to print the prime numbers less than a number.
"""

number = int(input("Enter a number: "))
print(f"Prime number less than {number} are :")
for num in range(2,number):
    for i in range(2,num):
        if num % i == 0:
            break
    else:
        print(num, end = " ")   # if for loop comletely finishes it comes to the "else" clause.(logic)














