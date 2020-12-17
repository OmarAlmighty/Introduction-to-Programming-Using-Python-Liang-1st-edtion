# 6.11 (Financial application: compute commissions) Write a function that computes
# the commission, using the scheme in Exercise 5.39. The header of the function is:
# def computeCommission(salesAmount):
# Write a test program that displays the following table:
# Sales Amount Commission
# 10000 900.0
# 15000 1500.0
# ...
# 95000 11100.0
# 100000 11700.0
from CH6Module import MyFunctions

print("Sales Amount\t\tCommission")

salesAmount = 10000
for i in range(1, 20):
    print(salesAmount, format(" ", "14s"), format(MyFunctions.computeCommission(salesAmount), ".1f"))
    salesAmount += 5000
