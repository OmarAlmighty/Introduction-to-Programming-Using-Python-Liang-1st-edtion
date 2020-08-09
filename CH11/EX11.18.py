# 11.18 (Shuffle rows) Write a function that shuffles the rows in a two-dimensional list
# using the following header:
# def shuffle(m):
# Write a test program that shuffles the following matrix:
# m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

import random


def shuffle(m):
    random.shuffle(m)


m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
shuffle(m)

print(m)
