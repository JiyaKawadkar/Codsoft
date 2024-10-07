import random
while True:
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    selection = int(input("Enter your Choice: "))
    if (selection == 1):
        player_choice = "Rock"
    elif (selection == 2):
        player_choice = "Paper"
    else:
        player_choice = "Scissors"
    print("Player's choice", player_choice)
    choice = ["Rock", "Paper", "Scissors"]
    Computer_choice = random.choice(choice)
    print("Computer choice", Computer_choice)
    if (player_choice == Computer_choice):
        print("Tie Game!")
    elif (player_choice == "Rock"):
        if (Computer_choice == "Paper"):
            print("Computer  Wins!")
        elif (Computer_choice == "Scissors"):
            print("Player Wins!")
    elif (player_choice == "Paper"):
        if (Computer_choice == "Scissors"):
            print(" Computer Wins!")
        elif (Computer_choice == "Rock"):
            print("Player Wins!")
    elif (player_choice == "Scissors"):
        if (Computer_choice == "Rock"):
            print("Computer Wins!")
        elif (Computer_choice == "Paper"):
            print("Player Wins!")
    print("1) Play Again")
    print("2) Quit")
    selection = int(input("Enter Choice: "))
    if (selection == 2):
        break
