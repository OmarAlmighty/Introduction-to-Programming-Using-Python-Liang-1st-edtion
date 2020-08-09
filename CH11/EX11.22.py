# 11.22 (Even number of 1s) Write a program that generates a two-dimensional
# matrix filled with 0s and 1s, displays the matrix, and checks to see if every row
# and every column has an even number of 1s.

import random


def main():
    n = 6
    matrix = []

    # Initialize matrix and display it
    for i in range(n):
        matrix.append([])
        for j in range(n):
            matrix[i].append(random.randint(0, 1))
            print(matrix[i][j], end=" ")

        print()

    if isEvenParity(matrix):
        print("All rows and columns are even")
    else:
        print("Not all rows and columns are even")


def isEvenParity(matrix):
    for i in range(len(matrix)):
        sum = 0
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
        if sum % 2 != 0:
            return False

    for j in range(len(matrix[0])):
        sum = 0
        for i in range(len(matrix)):
            sum += matrix[i][j]
        if sum % 2 != 0:
            return False

    return True


main()
