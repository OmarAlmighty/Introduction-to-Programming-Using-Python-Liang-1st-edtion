# 15.9 (Print the characters in a string reversely) Write a recursive function that displays
# a string reversely on the console using the following header:
# def reverseDisplay(value):
# For example, reverseDisplay("abcd") displays dcba. Write a test program
# that prompts the user to enter a string and displays its reversal.

def reverseDisplay(value):
    if value == '':
        print()
    else:
        print(value[-1], end='')
        reverseDisplay(value[:len(value) - 1])


val = input("Enter a string: ")
reverseDisplay(val)
