"""
Author - Pranav S Nair
Date - 19/11/2024
a python to program to help shop to manage its items details
"""

inventory = [
    ("Laptop",5,30000.00),
    ("Headphones",15,500.00),
    ("Mouse",50,150.00),
    ("Keyboard",20,150.00),
    ("Monitor",10,3000.00)
]
high_stock_value = 0
item_with_high_stock_value = None
for item in inventory:
    item_name, quantity, unit_Price = item    #unpacking tuple
    stock_value = quantity * unit_Price
    print(f"Item Name:{item_name},the stock value is {stock_value}")
    if stock_value > high_stock_value:
        high_stock_value = stock_value
        item_with_high_stock_value = item_name
print(f"Highest stock value is : {high_stock_value} ")
print(f"Item with highest stock value is {item_with_high_stock_value}")




