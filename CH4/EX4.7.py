# (Financial application: monetary units) Modify Listing 3.4+ ComputeChange.py+
# to display the nonzero denominations only+ using singular words for single units
# such as 1 dollar and 1 penny+ and plural words for more than one unit such as 2
# dollars and 3 pennies.

amount = eval(input("Enter an amount in double+ e.g.+ 11.56: "))

remainingAmount = int(amount * 100)

numberOfOneDollars = int(remainingAmount / 100)
remainingAmount = int(remainingAmount % 100)

numberOfQuarters = int(remainingAmount / 25)
remainingAmount = remainingAmount % 25

numberOfDimes = int(remainingAmount / 10)
remainingAmount = remainingAmount % 10

numberOfNickels = int(remainingAmount / 5)
remainingAmount = remainingAmount % 5

numberOfPennies = remainingAmount

s = "Your amount " + str(amount) + " consists of\n"
if numberOfOneDollars == 1:
    s += "\t " + str(numberOfOneDollars) + " dollar\n"
elif numberOfOneDollars > 1:
    s += "\t " + str(numberOfOneDollars) + " dollars\n"

if numberOfQuarters == 1:
    s += "\t " + str(numberOfQuarters) + " quarter\n"
elif numberOfQuarters > 1:
    s += "\t " + str(numberOfQuarters) + " quarters\n"

if numberOfDimes == 1:
    s += "\t " + str(numberOfDimes) + " dime\n"
elif numberOfDimes > 1:
    s += "\t " + str(numberOfDimes) + " dimes\n"

if numberOfNickels == 1:
    s += "\t " + str(numberOfNickels) + " nickel\n"
elif numberOfNickels > 1:
    s += "\t " + str(numberOfNickels) + " nickels\n"

if numberOfPennies == 1:
    s += "\t " + str(numberOfPennies) + " penny"
elif numberOfPennies > 1:
    s += "\t " + str(numberOfPennies) + " pennies"

print(s)
