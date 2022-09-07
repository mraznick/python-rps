import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

        # The following line will require the user to enter one of the three options in the List.
        # If they enter something else, the program will ask them again
    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_hand = options[random_number]
    print("Computer threw", computer_hand + ".")

    if user_input == "rock" and computer_hand == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_hand == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_hand == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_hand:
        print("Draw!")

    else:
        print("The robot won!")
        computer_wins += 1

print("You had", user_wins, "wins.")
print("The robot had", computer_wins, "wins.")
print("See you next time!")
