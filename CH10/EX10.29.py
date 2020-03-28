# 10.29 (Game: hangman) Write a hangman game that randomly generates a word and
# prompts the user to guess one letter at a time, as shown in the sample run. Each
# letter in the word is displayed as an asterisk. When the user makes a correct
# guess, the actual letter is then displayed. When the user finishes a word, display
# the number of misses and ask the user whether to continue playing. Create
# a list to store the words, as follows:
import random

words = ["write", "that", "program", "Hello"]

playAgain = 'y'
wrong = 0
while playAgain == 'y':
    w = words[random.randint(0,3)]
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
