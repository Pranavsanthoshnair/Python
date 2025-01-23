"""
Pranav S Nair
Date - 23/01/2025
Purpose - Kaprekars constant
"""

num = int(input("Enter a 4 digit number: "))
if num < 1000 or num > 9999:
    print("Invalid input")
else:
    count = 0
    while num != 6174:
        str_num = str(num)
        list = [int(i) for i in str_num]
        
        
        asc_list = sorted(list)
        desc_list = sorted(list, reverse=True)
        
        
        diff = (desc_list[0] - asc_list[0]) * 1000 + (desc_list[1] - asc_list[1]) * 100 + (desc_list[2] - asc_list[2]) * 10 + (desc_list[3] - asc_list[3])
        
        num = diff
        count += 1

    print("KAPREKAR CONSTANT REACHED!")
    print("The number of iterations is:", count)
