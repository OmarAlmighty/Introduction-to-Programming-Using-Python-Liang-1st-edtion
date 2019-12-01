# 8.7 (Phone keypads) The international standard letter/number mapping for telephones is
# Write a function that returns a number, given an uppercase letter, as follows:
# def getNumber(uppercaseLetter):
# Write a test program that prompts the user to enter a phone number as a string.
# The input number may contain letters.The program translates a letter(uppercase or lowercase)
# to a digit and leaves all other characters intact.

def getNumber(uppercaseLetter):
    if 'A' <= uppercaseLetter <= 'C':
        return 2
    elif 'D' <= uppercaseLetter <= 'F':
        return 3
    elif 'G' <= uppercaseLetter <= 'I':
        return 4
    elif 'J' <= uppercaseLetter <= 'L':
        return 5
    elif 'M' <= uppercaseLetter <= 'O':
        return 6
    elif 'P' <= uppercaseLetter <= 'S':
        return 7
    elif 'T' <= uppercaseLetter <= 'V':
        return 8
    elif 'W' <= uppercaseLetter <= 'Z':
        return 9


def main():
    s = input("Enter a string: ")
    res = ''
    for c in s:
        if c.isalpha():
            c = getNumber(c.upper())
        res = res + str(c)
    print(res)


main()
