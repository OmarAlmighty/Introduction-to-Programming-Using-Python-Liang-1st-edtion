# 6.35 (Compute the probability) Use the functions in RandomCharacter in Listing
# 6.11 to generate 10,000 uppercase letters and count the occurrence of A.

from random import randint  # import randint


# Generate a random character between ch1 and ch2
def getRandomCharacter(ch1, ch2):
    return chr(randint(ord(ch1), ord(ch2)))


# Generate a random uppercase letter
def getRandomUpperCaseLetter():
    return getRandomCharacter('A', 'Z')


def main():
    counter = 0
    for i in range(10000):
        c = getRandomUpperCaseLetter()
        print(c, end=' ')
        if c == 'A':
            counter += 1
        if (i + 1) % 10 == 0:
            print()

    print("\nNumber of generated As is", counter)


main()
