# 15.15 (Find the number of uppercase letters in a list) Write a recursive function to
# return the number of uppercase letters in a list of characters. You need to define
# the following two functions. The second one is a recursive helper function.
# def count(chars):
# def countHelper(chars, high):
# Write a test program that prompts the user to enter a list of characters in one line
# and displays the number of uppercase letters in the list.

def count(chars):
    return countHelper(chars, len(chars) - 1)


def countHelper(chars, high):
    count = 0
    if high >= 0:
        count = countHelper(chars, high - 1) + (1 if chars[high].isupper() else 0)

    return count


chars = input("Enter a list of chars: ").split()

print("The number of capital case letters is: ", count(chars))
