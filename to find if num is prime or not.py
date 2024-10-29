"""
Author - Pranav S Nair
Date - 29/10/2024
A Python Program to find if the inputted number by user is prime or not.
"""
num = int(input("Enter a number : "))
isPrime = True
for i in range(2,num//2+1):                              # i is a variable to note the no of iterations in the loop
    if num % i == 0:
        isPrime = False
        break
if isPrime:                                              # Here isPrime by default means that isPrime = True
    print(f"The given number {num} is Prime")
else:
    print(f"The given number {num} is not Prime")