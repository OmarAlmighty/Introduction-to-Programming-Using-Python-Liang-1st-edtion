# (Financial application: monetary units) Rewrite Listing 3.4, ComputeChange.py,
# to fix the possible loss of accuracy when converting a float value to an int value.
# Enter the input as an integer whose last two digits represent the cents. For example,
# the input 1156 represents 11 dollars and 56 cents.

amount = int(input("Enter an amount, for example, 1156: "))
numberOfOneDollars = amount // 100
amount = amount % 100
numberOfQuarters = amount // 25
amount = amount % 25
numberOfDimes = amount // 10
amount = amount % 10
numberOfNickels = amount // 5
amount = amount % 5
numberOfPennies = amount

print("Your amount", amount, "consists of\n",
      "\t", numberOfOneDollars, "dollars\n",
      "\t", numberOfQuarters, "quarters\n",
      "\t", numberOfDimes, "dimes\n",
      "\t", numberOfNickels, "nickels\n",
      "\t", numberOfPennies, "pennies")
