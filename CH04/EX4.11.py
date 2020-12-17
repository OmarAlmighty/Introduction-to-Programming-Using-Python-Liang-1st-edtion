# (Find the number of days in a month) Write a program that prompts the user to
# enter the month and year and displays the number of days in the month. For example,
# if the user entered month 2 and year 2000, the program should display that
# February 2000 has 29 days. If the user entered month 3 and year 2005, the program
# should display that March 2005 has 31 days.

month, year = eval(input("Enter month and year: "))
days = 0
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if month == 1:
    month = "January"
    days = 31
elif month == 2:
    month = "February"
    if isLeapYear:
        days = 29
    else:
        days = 28
elif month == 3:
    month = "March"
    days = 31
elif month == 4:
    month = "April"
    days = 30
elif month == 5:
    month = "May"
    days = 31
elif month == 6:
    month = "June"
    days = 30
elif month == 7:
    month = "July"
    days = 31
elif month == 8:
    month = "Augustus"
    days = 30
elif month == 9:
    month = "September"
    days = 31
elif month == 10:
    month = "October"
    days = 30
elif month == 11:
    month = "November"
    days = 31
elif month == 12:
    month = "December"
    days = 30

print(month, year, "has", days, "days")
