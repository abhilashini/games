import random
import re 


choices = {"R":"Rock", "P":"Paper", "S":"Scissors"}

while True:
    user_choice = input("Choose [R]ock, [P]aper or [S]cissors: ")
    
    if not re.match("[RrPpSs]", user_choice):
        print("Please choose one of [R]ock, [P]aper or [S]cissors")
        continue
    
    user_choice = user_choice.upper()[0]
    computer_choice = random.choice(list(choices.keys()))
    
    print("You picked {}. I picked {}".format(choices[user_choice], choices[computer_choice]))
    
    if user_choice.upper()[0] == computer_choice:
        print("It's a tie!")
    elif computer_choice == "R" and user_choice == "S":
        print("I win!")
    elif computer_choice == "S" and user_choice == "P":
        print("I win!")
    elif computer_choice == "P" and user_choice == "R":
        print("I win!")
    else:
        print("You win!")
