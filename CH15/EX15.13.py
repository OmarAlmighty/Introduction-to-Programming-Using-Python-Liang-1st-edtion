# 15.13 (Find the number of uppercase letters in a string) Write a recursive function to
# return the number of uppercase letters in a string using the following function
# headers:
# def countUppercase(s):
# def countUppercaseHelper(s, high):
# Write a test program that prompts the user to enter a string and displays the number
# of uppercase letters in the string.

count = 0


def countUppercase(s):
    return countUppercaseHelper(s, len(s))


def countUppercaseHelper(s, high):
    global count
    if s == '':
        return count

    if s[0].isupper():
        count += 1
    return countUppercaseHelper(s[1:high], high)


print(countUppercase(input("Enter a string: ")))
