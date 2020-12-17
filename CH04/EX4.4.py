# (Game: learn addition) Write a program that generates two integers under 100 and
# prompts the user to enter the sum of these two integers. The program then reports
# true if the answer is correct, false otherwise. The program is similar to Listing 4.1.
import random

n1, n2 = random.randint(0, 99), random.randint(0, 99)
s = "What is " + str(n1) + " + " + str(n2) + " ?"
res = eval(input(s))

print((res == (n1 + n2)))
