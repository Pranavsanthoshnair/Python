"""
Pranav S Nair
15/10/2024
A Python program that calculates the entry fee for the zoo based on the age entered by the user

"""

age = int(input("Enter your age : "))

if age<10:
    print("Fare is",7)
elif (age>=10 and age<60):
    print("Fare is",10)
else:
    print("Fare is",5)

