"""
Author - Pranav S Nair
Date - 14/11/2024
Purpose - A python program recreating the rock, paper and scissors game
"""

import random

player = input("Enter your name: ")
choices = ["Rock", "Paper", "Scissors"]

user_score = 0                                             #initialising user score
bot_score = 0                                              #initialising bot score

rounds = int(input("How many rounds would you like to play?: "))

for _ in range(rounds):                                    #The loop is to play game in multiple attempts
    bot_choice = random.choice(choices)
 
    while True:                                            #this loop is to check whether the entered prompt is in the given list
        user_choice = input("Enter 'Rock', 'Paper', OR 'Scissors': ")
        if user_choice in choices:
            break
        else:
            print("Invalid choice! Please enter 'Rock', 'Paper', or 'Scissors'.")

    print(f"{player} chooses {user_choice}")
    print(f"Bot chooses {bot_choice}")

    if user_choice == bot_choice:
        print("It's a draw!")
    elif (user_choice == "Rock" and bot_choice == "Scissors") or \
         (user_choice == "Scissors" and bot_choice == "Paper") or \
         (user_choice == "Paper" and bot_choice == "Rock"):
        print(f"{player} wins this round!")
        user_score += 1
    else:
        print("Bot wins this round!")
        bot_score += 1

print(f"\nFinal Scores after {rounds} rounds:")
print(f"{player}'s score: {user_score}")
print(f"Bot's score: {bot_score}")

if user_score > bot_score:
    print(f"{player} wins the game!")
elif user_score < bot_score:
    print("Bot wins the game!")
else:
    print("It's a tie!")
