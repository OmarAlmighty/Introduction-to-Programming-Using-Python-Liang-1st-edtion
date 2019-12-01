# 8.4 (Occurrences of a specified character) Write a function that finds the number of
# occurrences of a specified character in a string using the following header:
# def count(s, ch):
# The str class has the count method. Implement your method without using the
# count method. For example, count("Welcome", 'e') returns 2. Write a test
# program that prompts the user to enter a string followed by a character and displays
# the number of occurrences of the character in the string.

def main():
    str = input("Enter a string: ")
    ch = input("Enter a character to count: ")
    n = count(str, ch)
    print("Character", ch, "occurred", n, "times in", str)


def count(s, ch):
    counter = 0
    for c in s:
        if c == ch:
            counter += 1
    return counter


main()
