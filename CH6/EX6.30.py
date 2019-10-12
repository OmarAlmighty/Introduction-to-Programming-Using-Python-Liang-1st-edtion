# 6.30 (Game: chance of winning at craps) Revise Exercise 6.28 to run it 10,000 times
# and display the number of winning games.
from random import random


def main():
    winCount = 0

    for i in range(10000):
        dice = getDice()
        if dice == 7 or dice == 11:
            winCount += 1
        elif dice == 2 or dice == 3 or dice == 12:
            winCount += 0
        else:
            point = dice
            dice = getDice()
            # print("point is " + str(point))
            while dice != 7 and dice != point:
                dice = getDice()

            if dice != 7:
                winCount += 1

    print(winCount)


# Get a dice
def getDice():
    i1 = random.randint(1, 6)
    i2 = random.randint(1, 6)

    # print("You rolled " + str(i1) + " + " + str(i2) + " = " + str(i1 + i2))
    return i1 + i2


main()