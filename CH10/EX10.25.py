# 10.25 (Game: pick four cards) Write a program that picks four cards from a deck of 52
# cards and computes their sum. An ace, king, queen, and jack represent 1, 13, 12,
# and 11, respectively. Your program should display the number of picks that yield
# the sum of 24.
import random

cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
picks = []
s = 0
while True:
    for i in range(4):
        p = random.randint(1, 13)
        picks.append(p)

    s = sum(picks)
    if s == 24:
        print('The picks are', "(", cards[picks[0] - 1], ",",
              cards[picks[1] - 1], ",", cards[picks[2] - 1], ",", cards[picks[3] - 1], ")")
        break
    picks = []
