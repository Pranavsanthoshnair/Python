"""
Author - Pranav S Nair
Date - 19/11/2024
a python program to remove duplicates from a list
"""
my_list = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5]
unique_list = []      #created an empty list to append unique numbers from "my_list"

for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("The original list is",unique_list)
