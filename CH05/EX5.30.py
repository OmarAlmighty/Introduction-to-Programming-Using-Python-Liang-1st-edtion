# 5.30 (Display the first days of each month) Write a program that prompts the user
# to enter the year and first day of the year, and displays the first day of each month
# in the year on the console. For example, if the user entered year 2013, and 2 for
# Tuesday, January 1, 2013, your program should display the following output:
# January 1, 2013 is Tuesday
# ...
# December 1, 2013 is Sunday

year = eval(input("Enter a year: "))
firstDay = eval(input("Enter the first day of the year: "))
numberOfDaysInMonth = 0

for month in range(1, 13):
    if month == 1:
        print("January 1,", year, "is ", end="")
        numberOfDaysInMonth = 31
    elif month == 2:
        print("February 1,", year, "is ", end="")
        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
            numberOfDaysInMonth = 29
        else:
            numberOfDaysInMonth = 28
    elif month == 3:
        print("March 1,", year, "is ", end="")
        numberOfDaysInMonth = 31
    elif month == 4:
        print("April 1,", year, "is ", end="")
        numberOfDaysInMonth = 30
    elif month == 5:
        print("May 1,", year, "is ", end="")
        numberOfDaysInMonth = 31
    elif month == 6:
        print("June 1,", year, "is ", end="")
        numberOfDaysInMonth = 30
    elif month == 7:
        print("July 1,", year, "is ", end="")
        numberOfDaysInMonth = 31
    elif month == 8:
        print("August 1,", year, "is ", end="")
        numberOfDaysInMonth = 31
    elif month == 9:
        print("September 1,", year, "is ", end="")
        numberOfDaysInMonth = 30
    elif month == 10:
        print("October 1,", year, "is ", end="")
        numberOfDaysInMonth = 31
    elif month == 11:
        print("November 1,", year, "is ", end="")
        numberOfDaysInMonth = 30
    elif (month == 12):
        print("December 1,", year, "is ", end="")
        numberOfDaysInMonth = 31

    if firstDay == 0:
        print("Sunday")
    elif firstDay == 1:
        print("Monday")
    elif firstDay == 2:
        print("Tuesday")
    elif firstDay == 3:
        print("Wednesday")
    elif firstDay == 4:
        print("Thursday")
    elif firstDay == 5:
        print("Friday")
    elif firstDay == 6:
        print("Saturday")

    firstDay = (firstDay + numberOfDaysInMonth) % 7
