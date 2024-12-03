import random
def game_monty_hall():
    door_list =['1','2','3']
    host_choice = random.choice(door_list)
    gift_list = ["car","goat","goat"]
    random_gift_list = random.choice(gift_list)
    print(f"Welcome to the Monty Hall Game!")
    choice = (input("Choose a door (1,2 or 3): "))
    if choice not in door_list:
        print("Invalid Choice ! ")
    elif choice == 1 == gift_list[0]:
