# 13.7 (Game: hangman) Rewrite Exercise 10.29. The program reads the words stored
# in a text file named hangman.txt. Words are delimited by spaces.
import random

file = open('Words', 'r')
words = file.read().split()

playAgain = 'y'
wrong = 0
while playAgain == 'y':
    w = words[random.randint(0, len(words) - 1)]
    w = list(w)
    res = ['*'] * len(w)
    print("(Guess) Enter a letter in word", ''.join(res), end=' ')
    f = 0
    while True:
        guess = input()
        if guess not in res:
            if guess in w:
                for i in w:
                    if i == guess:
                        res[w.index(i)] = guess
                        w[w.index(i)] = '_'
                        if res.count('*') == 0:
                            f = 1
                            break
                if f == 1:
                    break
            else:
                wrong += 1
                print("\t", guess, "is not in the word")
        else:
            print("\t", guess, "is already in the word")
        print("(Guess) Enter a letter in word", ''.join(res), end=' ')

    print("The word is", ''.join(res))
    print("You have", wrong, "wrong guesses")
    wrong = 0
    playAgain = input("Do you want to play again (y or n) ").lower()
