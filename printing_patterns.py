"""
Author - Pranav S Nair
Date - 19/11/2024
a python program to print the patterns
"""
#Pattern 1
print("Increasing Triangle ")
no_of_row = int(input("Enter the number of columns : "))
for i in range(1,no_of_row+1):    # outer loop
    for j in range(i):                # inner loop
        print("*",end = ' ')
    print()

#Pattern 2
print("\nDecreasing Triangle ")
for i in range(no_of_row,0,-1):
    for j in range(i):
        print("*",end = ' ')
    print()

#Pattern 3
print("\nHill Pattern ")
for i in range(1,no_of_row+1):
    for j in range(no_of_row-i):
        print(" ",end = " ")
    for k in range(2 * i - 1):
        print("*",end = " ")
    print()

#Pattern 4
print("\nReverse Hill Pattern ")
for i in range(no_of_row,0,-1):
    for j in range(no_of_row-i):
        print(" ",end = " ")
    for k in range(2 * i - 1):
        print("*",end = " ")
    print()

