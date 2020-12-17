# 6.18 (Display matrix of 0s and 1s) Write a function that displays an n-by-n matrix using
# the following header:
# def printMatrix(n):
# Each element is 0 or 1, which is generated randomly. Write a test program that
# prompts the user to enter n and displays an n-by-n matrix.
import random


def printMatrix(n):
    for i in range(1, n * n + 1):
        x = random.randint(0, 1)
        print(x, end='  ')
        if i % n == 0:
            print()


def main():
    n = eval(input("Enter n: "))
    printMatrix(n)


main()
