import random
# Att göra fas 1:
# Välkomna användaren till spelet
# Läs in ett heltal från användaren
# Hårdkoda ett tal och lägga i en variabel
# Spelet går ut på att användaren ska gissa detta tal
# Efter varje input från användaren skal följande ske


 
# Att göra fas 2:



count = 0

# Skapa en meny
def show_menu():
    print("\n===========================================")
    print("|                  Welcome                |")
    print("|            To the number game           |")
    print("|         1. Start the game               |")
    print("|         q. Exit                         |")
    print("===========================================")

show_menu()
value = random.randint(0,10)
# Sätt en maxgräns för antalet gissningar innan spelet är över
menu_choice = (input("Make your choice, guess or exit: "))
while count != 5:
    # Håll ordning på (i en variabel) antalet chanser användaren behöver för att gissa
    count += 1
    try:
        if int(menu_choice) == 1:
            number_guess = (input(f"Guess the number! You have maximum 5 guesses, this is your {count} time: "))
            try:
                # Om det inmatade talet är större eller mindre än det talet användaren ska gissa, tala om det i så fall
                if int(number_guess) < value:
                    print("You are gessing to low, make another guess!\n ")
                elif int(number_guess) > value:
                    print("Your guess is to high, go again!\n ")
                else:
                    print("\nYou guessed the correct number, congratulations!!! Please try again if you like! \n Do you want to go again? (y/n) ")
                    if input("Make your choice ") == "y".str.lower:
                        count = 0
                    else:
                        print("Thanks for playing my game, you are welcome to play again at any time! ")
                        break     
                # else:
                #     print("Error, not valid input!")
            except:
                print("You can only enter a integer!")
        elif menu_choice == "q":
            print("Thanks for playing my game, welcome back!")
            break
        else:
            ("Test to input a integer instead!")
        if count == 5:
            print("Sorry, you're out of guesses!")
    except:
        print("Now something went really wrong here!")


