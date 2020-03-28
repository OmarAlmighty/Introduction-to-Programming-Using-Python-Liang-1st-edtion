# 10.22 (Simulation: coupon collector’s problem) Coupon Collector is a classic statistics
# problem with many practical applications. The problem is to pick objects from a
# set of objects repeatedly and find out how many picks are needed for all the
# objects to be picked at least once. A variation of the problem is to pick cards from
# a shuffled deck of 52 cards repeatedly and find out how many picks are needed
# before you see one of each suit. Assume a picked card is placed back in the deck
# before picking another. Write a program to simulate the number of picks needed
# to get four cards, one from each suit and display the four cards picked (it is possible
# a card may be picked twice).

import random


def main():
    NUMBER_OF_CARDS = 52
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9",
             "10", "Jack", "Queen", "King"]
    # found indicates whether a suit has been picked
    found = 4 * [False]

    # Count the number of picks
    numberOfPicks = 0

    # Count occurrence in each suit
    count = 0
    while count < 4:
        numberOfPicks += 1
        index = random.randint(0, NUMBER_OF_CARDS - 1)
        if not found[index // 13]:
            found[index // 13] = True
            count += 1

            suit = suits[index // 13]
            rank = ranks[index % 13]
            print(rank, "of", suit)

    print("Number of picks:", numberOfPicks)


main()
