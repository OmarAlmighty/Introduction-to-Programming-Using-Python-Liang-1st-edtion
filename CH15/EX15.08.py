# 15.8 (Print the digits in an integer reversely) Write a recursive function that displays
# an integer value reversely on the console using the following header:
# def reverseDisplay(value):
# For example, invoking reverseDisplay(12345) displays 54321. Write a test
# program that prompts the user to enter an integer and displays its reversal.

def reverseDisplay(value):
    if value == 0:
        print()
    else:
        print(value % 10, end='')
        reverseDisplay(value // 10)

val = eval(input("Enter an integer: "))
reverseDisplay(val)