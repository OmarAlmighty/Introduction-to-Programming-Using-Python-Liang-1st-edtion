# (Financial application: calculate future investment value) Write a program that
# reads in an investment amount, the annual interest rate, and the number of years,
# and displays the future investment value using the following formula:
# For example, if you enter the amount 1000, an annual interest rate of 4.25%,
# and the number of years as 1, the future investment value is 1043.33.

investAmount = eval(input("Enter investment amount:"))
annInterRate = eval(input("Enter annual interest rate:")) / (100 * 12)
numOfYears = eval(input("Enter number of years:")) * 12

futureVal = investAmount * (1 + annInterRate) ** numOfYears
print("Accumulated value is", futureVal)
