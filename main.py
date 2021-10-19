from random import randint
from game1 import number_game

def show_menu():
    print("\n===========================================")
    print("|                  Welcome                |")
    print("|        Do you want to play a game?      |")
    print("|        1. Enter the number game         |")
    print("|        2. Exit                          |")
    print("===========================================")

while True:
    random_value = randint(0,10)
    show_menu()
    try:
        menu_choice = int(input("Make your choice, guess or exit: "))
        if menu_choice == 1:
            number_game(random_value)
        elif menu_choice == 2:
            print("Thanks for playing, welcome back! ")
            break
        else:
            print("Thats a strange symbol, I can't seem to understand your input?")
    except ValueError:
        print("An error occurred, please try another input!")
