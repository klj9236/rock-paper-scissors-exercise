# game.py

print("Rock, Paper, Scissors, Shoot!")


# ask for a user input
x = input("Please choose either Rock, Paper, Scissors: ")
print(x)

# validate the user input

if (x == "Rock") or (x == "Paper") or (x == "Scissors"):
    print("Valid")
else: 
    print("Oops, invalid, please try again")
    exit()
print("Player Selected: ", x)

# simulating computer selection

import random
valid_options = ["Rock", "Paper", "Scissors"]
c = random.choice(valid_options)
print("Computer Selected: ", c)
