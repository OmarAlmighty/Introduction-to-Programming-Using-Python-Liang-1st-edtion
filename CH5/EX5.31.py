# 5.31 (Display calendars) Write a program that prompts the user to enter the year
# and first day of the year, and displays on the console the calendar table for the
# year. For example, if the user entered year 2005, and 6 for Saturday,
# January 1,42005, your program should display the calendar for each month in the year, as
# follows:

year = int(input("Enter a year: "))
day = int(input("Enter first Day of the year: "))

daysOfMonth = 0
for month in range(1, 13):
    print("\t", end='')

    if month == 1:
        print("\tJanuary", year)
        daysOfMonth = 31
    elif month == 2:
        print("\tFebruary ", year)
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            daysOfMonth = 29
        else:
            daysOfMonth = 28
    elif month == 3:
        print("\tMarch", year)
        daysOfMonth = 31
    elif month == 4:
        print("\tApril", year)
        daysOfMonth = 30
    elif month == 5:
        print("\tMay", year)
        daysOfMonth = 31
    elif month == 6:
        print("\tJune", year)
        daysOfMonth = 30
    elif month == 7:
        print("\tJuly", year)
        daysOfMonth = 31
    elif month == 8:
        print("\tAugust", year)
        daysOfMonth = 30
    elif month == 9:
        print("\tSeptember", year)
        daysOfMonth = 31
    elif month == 10:
        print("\tOctober", year)
        daysOfMonth = 30
    elif month == 11:
        print("\tNovember", year)
        daysOfMonth = 31
    elif month == 12:
        print("\tDecember", year)
        daysOfMonth = 31

    print("ـــــــــــــــــــــــــــ   ")
    print("   Sun Mon Tue Wed Thu Fri Sat")
    for i in range(0, day):
        print(format(" ", "4s"), end='')

    for i in range(1, daysOfMonth + 1):
        if i < 10:
            print(format(" ", "1s"), format(i, "2d"), end='')
        else:
            print(format(" ", "1s"), format(i, "2d"), end='')

        if (i + day) % 7 == 0:
            print()

    print("\n")
    day = (day + daysOfMonth) % 7
