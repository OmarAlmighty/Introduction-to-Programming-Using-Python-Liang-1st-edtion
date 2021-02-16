# 15.10 (Occurrences of a specified character in a string) Write a recursive function that
# finds the number of occurrences of a specified letter in a string using the following
# function header.
# def count(s, a):
# For example, count("Welcome", 'e') returns 2. Write a test program that
# prompts the user to enter a string and a character, and displays the number of
# occurrences for the character in the string.

counter = 0


def count(s, a):
    global counter
    if s == '':
        return counter
    elif s[0] == a:
        counter += 1
    return count(s[1:len(s)], a)


s, a = input("Enter a string and a character to count: ").split()
print("Character", a, "repeated", count(s.lower(), a.lower()), "times")
