# (Game: multiplication quiz) Listing 4.4, SubtractionQuiz.py, randomly generates
# a subtraction question. Revise the program to randomly generate a multiplication
# question with two integers less than 100.

import random

n1, n2 = random.randint(0, 99), random.randint(0, 99)
s = "What is " + str(n1) + " * " + str(n2) + " ? "
res = eval(input(s))

if res == (n1 * n2):
    print("You are correct!")
else:
    print("You are wrong")
    print(str(n1), "*", str(n2), "=", str(n1 * n2))