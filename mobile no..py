"""
Author - Pranav S Nair
Date - 30/11/2024
a python to program to check if a mobile number is valid or not
"""

def valid_mobile_no():
    mobile_no = input("Enter a mobile number: ")
    if len(mobile_no) == 10 and mobile_no[0] in ['7', '8', '9']:
        print(f"Mobile number {mobile_no} is valid")
    else:
        print(f"Mobile number {mobile_no} is invalid")

    return mobile_no


valid_mobile_no()

