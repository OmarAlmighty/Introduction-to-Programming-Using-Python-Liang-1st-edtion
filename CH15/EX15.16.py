# 15.16 (Occurrences of a specified character in a list) Write a recursive function that finds
# the number of occurrences of a specified character in a list. You need to define the
# following two functions. The second one is a recursive helper function.
# def count(chars, ch):
# def countHelper(chars, ch, high):
# Write a test program that prompts the user to enter a list of characters in one line,
# and a character, and displays the number of occurrences of the character in the list.

def count(chars, ch):
    return countHelper(chars, ch, len(chars) - 1)


def countHelper(chars, ch, high):
    count = 0
    if high >= 0:
        count = countHelper(chars, ch, high - 1) + (1 if chars[high] == ch else 0)

    return count


s, a = input("Enter a string and a character to count: ").split()
print("Character", a, "repeated", count(s.lower(), a.lower()), "times")
