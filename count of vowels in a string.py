"""
Author - Pranav S Nair
Date - 29/10/2024
A Python Program to count the no.of vowels in a string
"""
str_input = input("Enter a String : ")
vowels = "aeiouAEIOU"
count_vowels = 0
count_consonants = 0
for char in str_input:
    if char in vowels:
        count_vowels += 1
    else:
        count_consonants += 1
print(f"No of vowels in the given string {str_input} = {count_vowels} and No of consonants is {count_consonants}")