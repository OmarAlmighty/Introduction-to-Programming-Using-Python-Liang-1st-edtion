# 10.11 (Random number chooser) You can shuffle a list using random.shuffle(lst).
# Write your own function without using random.shuffle(lst) to shuffle a list
# and return the list. Use the following function header:
# def shuffle(lst):
# Write a test program that prompts the user to enter a list of numbers, invokes the
# function to shuffle the numbers, and displays the numbers.
import random


def shuffle(lst):
    for q in range(len(lst)):
        i, p = random.randint(0, len(lst)-1), random.randint(0, len(lst)-1)
        lst[i], lst[p] = lst[p], lst[i]

def main():
    lst = input("Enter numbers: ").split()
    lst = [int(x) for x in lst]
    shuffle(lst)
    print(lst)

main()