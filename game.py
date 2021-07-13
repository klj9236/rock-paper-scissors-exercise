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

# determining winner
if (x == "Rock") and (c == "Paper"):
    print("Computer Won")
elif (x == "Paper") and (c == "Rock"):
    print("You Won")
elif (x == "Paper") and (c == "Scissors"):
    print("Computer Won")
elif (x == "Scissors") and (c == "Paper"):
    print("You Won")
elif (x == "Rock") and (c == "Scissors"):
    print("You Won")
elif (x == "Scissors") and (c == "Rock"):
    print("Computer Won")
else:
    print("Tie")

# thank you message
print("Thanks for playing, please play again!")