"""
Author - Pranav S Nair
Date - 3/12/2024
a python program to create a stick game.
"""

def play_sticks_game():
    total_sticks = 16
    print("Welcome to the Sticks Game!")
    print("Rules: Players take turns to pick 1, 2, or 3 sticks. The player who picks the last stick loses.")
    print("The game starts with 16 sticks.")

    # Get player names
    player1 = input("Enter the name of PLAYER 1: ")
    player2 = input("Enter the name of PLAYER 2: ")

    current_player = player1  # Start with player 1

    while total_sticks > 0:
        print(f"\nSticks remaining: {total_sticks}")
        try:
            pick = int(input(f"{current_player}, pick 1, 2, or 3 sticks: "))
            if 1 <= pick <= 3 and pick <= total_sticks:
                total_sticks -= pick
                if total_sticks == 0:
                    print(f"\n{current_player} picks the last stick and loses the game.")
                    break

                # Switch player
                current_player = player2 if current_player == player1 else player1
            else:
                print("Invalid choice! You must pick between 1 and 3 sticks, and not more than the remaining sticks.")
        except ValueError:
            print("Invalid input! Please enter a number.")

    print("Game Over!")

# Start the game
play_sticks_game()





