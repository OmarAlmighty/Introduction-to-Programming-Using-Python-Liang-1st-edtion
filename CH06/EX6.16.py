# 6.16 (Number of days in a year) Write a function that returns the number of days in a
# year using the following header:
# def numberOfDaysInAYear(year):
# Write a test program that displays the number of days in the years from 2010 to
# 2020.
from CH6Module import MyFunctions

for year in range(2010, 2021):
    print(year, "has", MyFunctions.numberOfDaysInAYear(year))