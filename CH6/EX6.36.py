# 6.36 (Generate random characters) Use the functions in RandomCharacter in
# Listing 6.11 to print 100 uppercase letters and then 100 single digits, printing ten
# per line.
# Generate a random digit character
from random import randint


def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


def getRandomDigitCharacter():
    return getRandomCharacter('0', '9')


# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')


def main():
    for i in range(100):
        c = getRandomUpperCaseLetter()
        print(c, end=' ')
        if (i + 1) % 10 == 0:
            print()
    print()

    for i in range(100):
        c = getRandomDigitCharacter()
        print(c, end=' ')
        if (i + 1) % 10 == 0:
            print()

main()