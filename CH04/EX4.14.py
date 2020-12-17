# 4.14 (Game: heads or tails) Write a program that lets the user guess whether a flipped
# coin displays the head or the tail. The program randomly generates an integer 0 or
# 1, which represents head or tail. The program prompts the user to enter a guess
# and reports whether the guess is correct or incorrect.
import random

g = random.randint(0, 1)
guess = int(input("Guess Head(0) or Tail(1): "))

if g == guess:
    print("You are right. The guess is ", end="Head" if g == 0 else "Tail")
else:
    print("Wrong. The guess is ", end="Head" if g == 0 else "Tail")
