"""
Rock, Paper and Scissor Games
"""

import random
import sys
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")

machine = random.randint(0, 3)
player = random.randint(0, 3)
ROCK = 0
PAPER = 1
SCISSORS = 2

# *when the choices is not exist
if player not in [0, 1, 2]:
    print("Your choices is not valid")
    sys.exit()


# *when players has the same choices
if machine == player:
    print("It was a draw")
    sys.exit()
print(f"Machine choices: {machine}, player choices: {player}")

# *when rock wins
if machine == ROCK and player == SCISSORS:
    print("The machine wins")

# *when paper win
elif machine == PAPER and player == ROCK:
    print("machine win")

# *when scissors win
elif machine == SCISSORS and player == PAPER:
    print("machine win")
else:
    print("You're win")
