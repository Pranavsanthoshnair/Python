"""
Author - Pranav S Nair
Date - 14/11/2024
Purpose - A python program of a number guessing game"""
import random
guess = random.randint(1,100)
no_of_tries = 0
while True:
    no_of_tries += 1
    num = int(input("Enter any number from 1 to 100: "))
    if(num == guess):
        print(f"Hurray!,The guessed number {num} is correct.")
        break
    elif(num>guess):
        print(f"Oops!,The guessed number is big, try a smaller number.")
    elif(num<guess):
        print(f"Oops!,The guessed number is small, try a bigger number.")
    
print(f"No.of tries = {no_of_tries}")