# 5.33 (Financial application: compute CD value) Suppose you put $10,000 into a CD
# with an annual percentage yield of 5.75%. After one month, the CD is worth
# 10000 + 10000 * 5.75 / 1200 = 10047.91
# After two months, the CD is worth
# 10047.91 + 10047.91 * 5.75 / 1200 = 10096.06
# After three months, the CD is worth
# 10096.06 + 10096.06 * 5.75 / 1200 = 10145.43
# and so on.
# Write a program that prompts the user to enter an amount (e.g., 10,000), the
# annual percentage yield (e.g., 5.75), and the number of months (e.g., 18), and displays
# a table as shown in the sample run.

initialDepositAmount = eval(input("Enter the initial deposit amount: "))
annualPercentageYield = eval(input("Enter annual percentage yield: "))
period = eval(input("Enter maturity period (number of months): "))

print("Month    CD value")
val = initialDepositAmount
for i in range(1, period + 1):
    val = val + val * annualPercentageYield / 1200
    print(format(i,"2d"), format(" ", "5s"), format(val, "-4.2f"))
