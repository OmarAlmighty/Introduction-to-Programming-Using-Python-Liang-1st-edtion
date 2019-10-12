# 6.15  (Financial application: print a tax table)  Listing 4.7, ComputeTax.py, gives a
# program to compute tax. Write a function for computing tax using the following
# header:
# def computeTax (status, taxableIncome ):
# Use this function to write a program that prints a tax table for taxable income from
# $50,000 to $60,000 with intervals of $50 for all four statuses, as follows:
# Taxable Single Married Married Head of
# Income Joint Separate a House
# 50000 8688 6665 8688 7352
# 50050 8700 6673 8700 7365
# ...
# 59950 11175 8158 11175 9840
# 60000 11188 8165 11188 9852
from CH6Module import MyFunctions

print("Taxable\t\tSingle\t\tMarried\t\tMarried\t\tHead of")
print("Income\t\t\t\t\tJoint\t\tSeparate\ta House")

for i in range(50000, 60001, 50):
    print(i, "\t   ", MyFunctions.computeTax(0, i), "\t", MyFunctions.computeTax(1, i),
          "\t", MyFunctions.computeTax(2, i), "\t", MyFunctions.computeTax(3, i))
