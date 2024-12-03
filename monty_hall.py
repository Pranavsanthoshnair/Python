"""
Author - Pranav S Nair
Date - 3/12/2024
A python program of the game ;monty hall'
"""
import random

def game_monty_hall():
    print("Welcome to the Monty Hall Game!")
    print("There are 3 doors: Behind one is a car, and behind the other two are goats.")
    print("You will pick a door, and the host will reveal a goat behind one of the other doors.")
    print("Then, you can choose to switch doors or stay with your choice.")

    doors = ['1', '2', '3']
    prizes = ['car', 'goat', 'goat']
    random.shuffle(prizes)  # Randomize the prize locations

    # Player's choice
    player_choice = input("Choose a door (1, 2, or 3): ")
    if player_choice not in doors:
        print("Invalid choice! Please restart and choose a valid door.")
        return

    player_index = doors.index(player_choice)  # Find the index of the chosen door

    # Host reveals a goat from the remaining doors
    for i in range(3):
        if i != player_index and prizes[i] == 'goat':  # Find a door with a goat
            host_reveal = doors[i]
            break
    print(f"The host opens door {host_reveal} to reveal a goat.")

    # Determine the remaining door that the player could switch to
    if player_choice == '1' and host_reveal != '2':
        remaining_door = '2'
    elif player_choice == '1' and host_reveal != '3':
        remaining_door = '3'
    elif player_choice == '2' and host_reveal != '1':
        remaining_door = '1'
    elif player_choice == '2' and host_reveal != '3':
        remaining_door = '3'
    elif player_choice == '3' and host_reveal != '1':
        remaining_door = '1'
    elif player_choice == '3' and host_reveal != '2':
        remaining_door = '2'

    # Ask if the player wants to switch doors
    switch = input(f"Do you want to switch to door {remaining_door}? (yes or no): ").lower()

    if switch == 'yes':
        player_choice = remaining_door

    final_prize = prizes[doors.index(player_choice)]

    if final_prize == 'car':
        print(f"Congratulations! You chose door {player_choice} and won a car!")
    else:
        print(f"Sorry, you chose door {player_choice} and got a goat.")

    print("Thanks for playing!")

game_monty_hall()
