# 5.23 (Financial application: compare loans with various interest rates) Write a program
# that lets the user enter the loan amount and loan period in number of years
# and displays the monthly and total payments for each interest rate starting from
# 5% to 8%, with an increment of 1/8.
import math

loanAmount = eval(input("Loan Amount: "))
years = eval(input("Number of Years: "))

print("Interest Rate    Monthly Payment    Total Payment")
i = years
counter = 1
while counter < 26:
    print(format(i, "-5.3f"), end='%')
    print("         ", end='')
    monthlyInterestRate = i / 1200
    monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / math.pow(1 + monthlyInterestRate, years * 12))
    print(format(monthlyPayment, "-5.2f"), end='')
    print(format((monthlyPayment * 12) * years, "-24.2f"))
    counter += 1
    i += .125
