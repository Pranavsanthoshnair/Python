"""
Author - Pranav S Nair
Date - 12/11/2024
Purpose - A Python program that iterates through integers from 1 to 50. For each multiple of three, print "Fizz" instead of the number; for each multiple of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".
"""

for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("Fizzbuzz")
    elif fizzbuzz % 3 == 0:
       print("fizz")
    elif fizzbuzz % 5 == 0:
        print("buzz")
    else:
        print(fizzbuzz)
    