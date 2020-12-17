# 8.6 (Count the letters in a string) Write a function that counts the number of letters in
# a string using the following header:
# def countLetters(s):
# Write a test program that prompts the user to enter a string and displays the number
# of letters in the string.

def countLetters(s):
    counter = 0
    for c in s:
        if c.isalpha():
            counter += 1
    return counter


def main():
    s = input("Enter a string: ")
    n = countLetters(s)
    print("Number of letters is", n)

main()