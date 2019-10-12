# 6.28 (Game: craps) Craps is a popular dice game played in casinos. Write a program to
# play a variation of the game, as follows:
# Roll two dice. Each die has six faces representing values 1, 2, ..., and 6, respectively.
# Check the sum of the two dice. If the sum is 2, 3, or 12 (called craps), you
# lose; if the sum is 7 or 11 (called natural), you win; if the sum is another value
# (i.e., 4, 5, 6, 8, 9, or 10), a point is established. Continue to roll the dice until either
# a 7 or the same point value is rolled. If 7 is rolled, you lose. Otherwise, you win.
# Your program acts as a single player.
import sys
from random import random


def main():
    dice = getDice()
    if dice == 7 or dice == 11:
        print("You win")
        sys.exit()
    elif dice == 2 or dice == 3 or dice == 12:
        print("You lose")
        sys.exit()

    point = dice
    print("point is", point)

    dice = getDice()
    while dice != 7 and dice != point:
        dice = getDice()

    if dice == 7:
        print("You lose")
    else:
        print("You win")


# Get a dice
def getDice():
    i1 = random.randint(1, 6)
    i2 = random.randint(1, 6)

    print("You rolled", i1, "+", i2, "=", i1 + i2)
    return i1 + i2
