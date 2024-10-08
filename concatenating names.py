"""
 A Program to Create, concatenate, and print a string and access a sub-string from a given string.
Author - Pranav S Nair
Date - 08/10/2024
"""


first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
full_name = first_name + " " + last_name

length = len(first_name)
extracted_first_name = full_name[:length]
print(full_name)
print(extracted_first_name)
