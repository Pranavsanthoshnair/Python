"""
Author - Pranav S Nair
Date - 30/11/2024
a python to program to check the no.of uppercase and lower case characters in a string
"""

sample_str = input("Enter a string : ")
def check_case_of_str():
    str = sample_str.replace(" ","")       # since IDE counts space as lower case characters"
    no_of_uppercase = 0
    no_of_lowercase = 0
    for char in str:
        if char.isupper():
            no_of_uppercase += 1
        else:
            no_of_lowercase += 1
    return no_of_uppercase,no_of_lowercase

no_of_uppercase,no_of_lowercase = check_case_of_str()    # unpacking the tuple since multiple values come in the form of a tuple

print(f"No.of uppercase letters is {no_of_uppercase} ")
print(f"No.of lowercase letters is {no_of_lowercase} ")