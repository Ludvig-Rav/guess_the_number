import random

count = 0
number0 = 1
number1 = 10
no_of_guesses = 5

def show_menu():
    print("\n===========================================")
    print("|                  Welcome                |")
    print("|        Do you want to play a game?      |")
    print("|        1. Enter the number game         |")
    print("|        2. Exit                          |")
    print("===========================================")

def number_game_menu():
    print("\n===========================================")
    print("|                  Welcome                |")
    print("|            To the number game           |")
    print("|         s. Start                        |")
    print("|         q. Exit                         |")
    print("===========================================")

def number_game(rand_number):
    number_game_menu()
    user_choice = str(input(""))
    if user_choice == 's':
        counter = 0
        print(f"The number you are looking for is a number between {number0} and {number1}\nYou have {no_of_guesses} times to make a guess\n")
        while True:
            counter += 1
            if counter == no_of_guesses:
                choice = input("Sorry, you're out of guesses...\nDo you want to try again? y/n ")
                if choice == "y":
                    counter = 0
                else:
                    break
            user_guess = int(input(f"What is your {counter} guess? "))
            if user_guess < rand_number:
                print("You are gessing to low, make another guess!\n ")
            elif user_guess > rand_number:
                print("Your guess is to high, go again!\n ")
            else:
                print("\nYou guessed the correct number, congratulations!!! Please try again if you like! \n Do you want to go again? (y/n) ")
                if input("Make your choice ") == "y":
                    print("Go again")  
                    counter = 0
                else:
                    print("Thanks for playing my game, you are welcome to play again at any time! ")
                    break
    else:
        print("Leaving the game")
    print("Thanks for playing, you'll be redirected to the start menu.")
        
    # while True:
    #     count += 1
    #     try:
    #         if int(menu_choice) == 1:
    #             number_guess = (input(f"Guess the number! You have maximum 5 guesses, this is your {count} time: "))
    #             try:
    #                 if int(number_guess) < rand_number:
    #                     return "You are gessing to low, make another guess!\n "
    #                 elif int(number_guess) > rand_number:
    #                     return "Your guess is to high, go again!\n "
    #                 else:
    #                     print("\nYou guessed the correct number, congratulations!!! Please try again if you like! \n Do you want to go again? (y/n) ")
    #                     if input("Make your choice ") == "y".str.lower:
    #                         count = 0
    #                     else:
    #                         print("Thanks for playing my game, you are welcome to play again at any time! ")
    #                         break     
    #             except:
    #                 print("You can only enter a integer!")
    #         elif menu_choice == "q":
    #             print("Thanks for playing my game, welcome back!")
    #             break
    #         else:
    #             ("Test to input a integer instead!")
    #         if count == 5:
    #             print("Sorry, you're out of guesses!")
    #     except:
    #         print("Now something went really wrong here!")



while True:
    random_value = random.randint(0,10)
    show_menu()
    menu_choice = int(input("Make your choice, guess or exit: "))
    if menu_choice == 1:
        number_game(random_value)
    elif menu_choice == 2:
        print("Thanks for playing, welcome back! ")
        break
    else:
        print("Thats a strange symbol, I can't seem to understand your input?")
