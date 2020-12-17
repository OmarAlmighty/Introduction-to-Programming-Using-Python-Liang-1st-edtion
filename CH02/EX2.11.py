# (Financial application: investment amount) Suppose you want to deposit a
# certain amount of money into a savings account with a fixed annual interest rate.
# What amount do you need to deposit in order to have $5,000 in the account after
# three years? The initial deposit amount can be obtained using the following
# formula:
# Write a program that prompts the user to enter final account value, annual interest
# rate in percent, and the number of years, and displays the initial deposit amount.

finAccVal = eval(input("Enter final account value: "))
monthInterRatePerc = eval(input("Enter annual interest rate in percent: ")) / (100 * 12)
numOfMonths = eval(input("Enter number of years: ")) * 12
initialDepositAmount = finAccVal / (1 + monthInterRatePerc) ** numOfMonths
print("Initial deposit value is", initialDepositAmount)
