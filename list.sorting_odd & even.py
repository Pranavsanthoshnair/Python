"""
Author - Pranav S Nair
Date - 19/11/2024
a python program to sort first even numbers and then odd numbers from 2 given lists.
"""
num_of_list1 = int(input("Enter how many elements are there in list 1: "))

list1 = []
list2 = []
#Forming list1
for i in range(num_of_list1):
    list1.append(int(input("Enter elements of list 1 : ")))

num_of_list2 = int(input("Enter how many elements are there in list 2: "))
#Forming list2
for j in range(num_of_list2):
    list2.append(int(input("Enter elements of list 2 : ")))

combined_list = (list1+list2)  #creating a combined list

even_list = []
odd_list = []

for k in combined_list:
    if k % 2 == 0:                    # to separate even numbers into "even_list"
        even_list.append(k)
    else:                             # to separate odd numbers into "odd_list"
        odd_list.append(k)

even_list.sort()
odd_list.sort()

merged_list = (even_list + odd_list)            # merging the sorted "even_list" & "odd_list"
print(merged_list)


