# (Financial application: payroll) Write a program that reads the following information
# and prints a payroll statement:
# Employee’s name (e.g., Smith)
# Number of hours worked in a week (e.g., 10)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)

name = input("Enter employee's name: ")
workH = eval(input("Enter number of hours worked in a week: "))
payR = eval(input("Enter hourly pay rate: "))
ftwr = eval(input("Enter federal tax withholding rate: "))
stwr = eval(input("Enter state tax withholding rate: "))
grossP = workH * payR
fw = .2 * grossP
sw = stwr * grossP
total = fw + sw
net = grossP - total

print("Employee Name:", format(name, "2s"))
print("Hours Worked:", format(workH, ".1f"))
print("Pay Rate:", format(payR, ".2f"))
print("Gross Pay:", format(grossP, ".1f"))
print("Deductions:")
print("\tFederal Withholding " + "(" + format(ftwr, "2.1%") + "): $" + format(fw, ".2f"))
print("\tState Withholding " + "(" + format(stwr, ".1%") + "): $" + format(sw, ".2f"))
print("\tTotal Deduction: " + "$" + format(total, ".2f"))
print("Net Pay: $" + format(net, ".2f"))
