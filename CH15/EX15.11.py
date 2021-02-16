# 15.11 (Print the characters in a string reversely) Rewrite Exercise 15.9 using a helper
# function to pass the substring for the high index to the function. The helper
# function header is:
# def reverseDisplayHelper(s, high):

def reverseDisplay(value):
    reverseDisplayHelper(value, len(value) - 1)


def reverseDisplayHelper(s, high):
    if high < 0:
        print()
    else:
        print(s[high], end='')
        reverseDisplayHelper(s, high - 1)


val = input("Enter a string: ")
reverseDisplay(val)
