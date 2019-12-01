# 8.11 (Reverse a string) Write a function that reverses a string. The header of the function
# is:
# def reverse(s):
# Write a test program that prompts the user to enter a string, invokes the reverse
# function, and displays the reversed string.
def reverse(s):
    new = s[len(s):0:-1] + s[0]
    return new


def main():
    st = input("Enter a string: ")
    print("The reverse of", st, "is", reverse(st))


main()
