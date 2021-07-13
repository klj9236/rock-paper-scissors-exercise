# game.py

print("Rock, Paper, Scissors, Shoot!")


# ask for a user input
x = input("Please choose either 'rock, 'paper', 'scissors'")
print(x)

# validate the user input

if (x == "rock") or (x == "paper") or (x == "scissors"):
    print("valid")
else: 
    print("Oops, invalid, please try again")
exit()
print("later messages")
