import random


choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

while True:
    user_choice = input("Choose Rock, Paper, Scissors, Lizard or Spock - ").capitalize()
    
    if user_choice not in choices:
        print("Please choose one of the following: ")
        continue
    
    computer_choice = random.choice(choices)
    
    print("You picked {}. I picked {}".format(user_choice, computer_choice))
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif computer_choice == "Lizard" and (user_choice == "Spock" or user_choice == "Paper"):
        print("I win!")
    elif computer_choice == "Spock" and (user_choice == "Scissors" or user_choice == "Rock"):
        print("I win!")
    elif computer_choice == "Scissors" and (user_choice == "Lizard" or user_choice == "Paper"):
        print("I win!")
    elif computer_choice == "Paper" and (user_choice == "Spock" or user_choice == "Rock"):
        print("I win!")
    elif computer_choice == "Rock" and (user_choice == "Lizard" or user_choice == "Scissors"):
        print("I win!")
    else:
        print("You win!")
