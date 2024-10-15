"""
Pranav S Nair
15/10/2024
A Python program that calculates the dicounted amount based on the total amount entered by the user.
"""

bill_amount = float(input("Enter the bill amount : "))


if bill_amount > 500:
    print("Total amount is ",bill_amount-(0.2*bill_amount))
elif (200 <= bill_amount <= 500):
    print("Total amount is ",bill_amount-(0.1*bill_amount))
else:
    print("Total amount is ",bill_amount)
