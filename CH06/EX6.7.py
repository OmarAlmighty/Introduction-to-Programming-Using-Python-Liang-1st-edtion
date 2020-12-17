# 6.7 (Financial application: compute the future investment value) Write a function that
# computes a future investment value at a given interest rate for a specified number of
# years. The future investment is determined using the formula in Exercise 2.19.
# Use the following function header:
# def futureInvestmentValue(
# investmentAmount, monthlyInterestRate, years):
# For example, futureInvestmentValue(10000, 0.05/12, 5) returns
# 12833.59.
# Write a test program that prompts the user to enter the investment amount and the
# annual interest rate in percent and prints a table that displays the future value for
# the years from 1 to 30.

def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    print("Years       Future years")
    for i in range(1, years + 1):
        futureValue = investmentAmount * ((1 + monthlyInterestRate) ** (12 * i))
        print(i, "\t\t\t", format(futureValue, ".2f"))


def main():
    investmentAmount = eval(input("The amount invested : "))
    interestRate = eval(input("Annual interest rate : "))
    futureInvestmentValue(investmentAmount, interestRate / 1200, 30)


main()
