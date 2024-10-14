"""
Python program that calculates the grade based on the score entered by the user
Author - Pranav S Nair
Date - 09-10-2024
"""



days = int(input("Input days : ")) * 60 * 60 * 24
hours = int(input("Input hours : ")) * 60 * 60
minutes = int(input("Input minutes : ")) * 60
seconds = int(input("Input seconds : "))



time = days + hours + minutes + seconds
print("The amount of the seconds",time)