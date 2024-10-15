"""
Pranav S Nair
15/10/2024
A Python program that determines the simple interest based on the values entered by the user
"""


p = float(input("Enter Principal Amount : "))
n = float(input("Enter No.of Years : "))
r = float(input("Enter Rate of interest : "))

simple_interest = (p*n*r)/100   # Here rate of interest will be in percentage so we should divide simple interest by 100
print(simple_interest)