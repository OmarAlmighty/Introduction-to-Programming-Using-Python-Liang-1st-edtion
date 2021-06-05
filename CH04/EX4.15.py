# 4.15 (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a three-digit lottery
# number. The program prompts the user to enter a three-digit number and determines
# whether the user wins according to the following rules:
# 1. If the user input matches the lottery number in the exact order, the award is
# $10,000.
# 2. If all the digits in the user input match all the digits in the lottery number, the
# award is $3,000.
# 3. If one digit in the user input matches a digit in the lottery number, the award is
# $1,000.
import random

num = random.randint(100, 999)
print(str(num))
guess = int(input("Enter 3 digit number: "))

NUM = num
GUESS = guess
g1 = GUESS // 100
GUESS %= 100
g2 = GUESS // 10
GUESS %= 10
g3 = GUESS

n1 = NUM // 100
NUM %= 100
n2 = NUM // 10
NUM %= 10
n3 = NUM

if num == guess:
    print("Exact match. You won $10,000")
elif (  g1 == n1 and g3 == n2 and g2 == n3 or
        g2 == n1 and g1 == n2 and g3 == n3 or
        g2 == n1 and g3 == n2 and g1 == n3 or
        g3 == n1 and g1 == n2 and g2 == n3 or
        g3 == n1 and g2 == n2 and g1 == n3):
    print("Match all digits: you win $3,000")
elif (g1 == n2 or g1 == n3
      or g2 == n1 or g2 == n3
      or g3 == n1 or g3 == n2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")