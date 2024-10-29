"""
Author - Pranav S Nair
Date - 29/10/2024
A Python Program to process the output of prime numbers upto 'n'(inputted by user).
"""
limit = int(input("Enter limit : "))
for i in range (2,limit+1):
    isPrime = True
    for j in range (2,(i//2)+1):
        if i % j == 0:
            isPrime = False
    if isPrime:
        print(i,end = " ")                             # i and j are variables to note the No:of iterations in the loop