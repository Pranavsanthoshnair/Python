"""
A Python program that calculates the grade according to the score entered by the user
Author - Pranav S Nair
Date - 15/10/2024
"""


score = float(input("Enter your score : "))

if(score >= 90):
    print("A")
elif(score >= 80):
    print("B")
elif(score >= 70):
    print("C")
elif(score >= 60):
    print("D")
elif(score >= 50):
    print("E")
elif(score >= 0):
    print("Fail")
else:
    print("Invalid Score")



