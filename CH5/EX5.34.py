# 5.34 (Game: lottery) Revise Listing 4.10, Lottery.py, to generate a lottery of a two-digit
# number. The two digits in the number are distinct. (Hint: Generate the first digit.
# Use a loop to continuously generate the second digit until it is different from the
# first digit.)

import random

guessDigit1 = lotteryDigit1 = random.randint(0, 9)
lotteryDigit2 = random.randint(0, 9)

while lotteryDigit1 == lotteryDigit2:
    lotteryDigit2 = random.randint(0, 9)

guess = eval(input("Enter your lottery pick (two digits): "))

guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is ", lotteryDigit1, lotteryDigit2)

if guessDigit1 == lotteryDigit1 and guessDigit2 == lotteryDigit2:
    print("Exact match: you win $10,000")
elif guessDigit2 == lotteryDigit1 and guessDigit1 == lotteryDigit2:
    print("Match all digits: you win $3,000")
elif (guessDigit1 == lotteryDigit1
      or guessDigit1 == lotteryDigit2
      or guessDigit2 == lotteryDigit1
      or guessDigit2 == lotteryDigit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, no match")

