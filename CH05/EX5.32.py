# 5.32 (Financial application: compound value) Suppose you save $100 each month into
# a savings account with the annual interest rate 5%. So, the monthly interest rate is
# After the first month, the value in the account becomes
# 100 * (1 + 0.00417) = 100.417
# After the second month, the value in the account becomes
# (100 + 100.417) * (1 + 0.00417) = 201.252
# After the third month, the value in the account becomes
# (100 + 201.252) * (1 + 0.00417) = 302.507
# and so on.
# Write a program that prompts the user to enter an amount (e.g., 100), the annual
# interest rate (e.g., 5), and the number of months (e.g., 6), and displays the amount
# in the savings account after the given month.

monthlyDeposit = eval(input("Enter the amount to be saved for each month: "))
annualIR = eval(input("Enter the annual interest rate: "))
monthlyIR = annualIR / 1200
months = eval(input("Enter the number of months: "))

value = monthlyDeposit * (1 + monthlyIR)
for i in range(1, months):
    value = (value + monthlyDeposit) * (1 + monthlyIR)

print("After the", months, "th month, the account value is ", value)
