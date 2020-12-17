# 6.31 (Current date and time) Invoking time.time() returns the elapsed time in seconds
# since midnight of January 1, 1970. Write a program that displays the date
# and time.
import time


def main():
    currentTime = time.time()  # Get current time

    # Obtain the total seconds since midnight, Jan 1, 1970
    totalSeconds = int(currentTime)

    # Get the current second
    currentSecond = totalSeconds % 60

    # Obtain the total minutes
    totalMinutes = totalSeconds // 60

    # Compute the current minute in the hour
    currentMinute = totalMinutes % 60

    # Obtain the total hours
    totalHours = totalMinutes // 60

    # Compute the current hour
    currentHour = totalHours % 24

    # Compute the total days
    totalDays = totalHours // 24
    if currentHour > 0:
        totalDays += 1

    # Obtain Year
    currentYear = 2000
    while getTotalDaysInYears(currentYear) < totalDays:
        currentYear += 1

    # Obtain Month
    totalNumOfDaysInTheYear = totalDays - getTotalDaysInYears(currentYear - 1)
    currentMonth = 0
    while getTotalDaysInMonths(currentYear, currentMonth) < totalNumOfDaysInTheYear:
        currentMonth += 1

    monthName = getMonthName(currentMonth)
    # Obtain Day
    currentDay = totalNumOfDaysInTheYear - getTotalDaysInMonths(currentYear, currentMonth - 1)

    # Display results
    output = "Current date and time is " + \
             monthName + " " + str(currentDay) + "," + str(currentYear) + " " + \
             str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond)

    print(output)


# Get the total number of days from Jan 1, 1970 to the specified year
def getTotalDaysInYears(year):
    total = 0

    # Get the total days from 1970 to the specified year
    for i in range(1970, year + 1):
        if isLeapYear(i):
            total = total + 366
        else:
            total = total + 365

    return total


# Get the total number of days from Jan 1 to the month in the year*
def getTotalDaysInMonths(year, month):
    total = 0

    # Add days from Jan to the month
    for i in range(1, month + 1):
        total = total + getNumberOfDaysInMonth(year, i)

    return total


# Get the number of days in a month
def getNumberOfDaysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or \
            month == 8 or month == 10 or month == 12:
        return 31

    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30

    if month == 2:
        return 29 if isLeapYear(year) else 28

    return 0  # If month is incorrect


# Determine if it is a leap year
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def getMonthName(currentMonth):
    monthName = ""
    if currentMonth == 1:
        monthName = "January"
    elif currentMonth == 2:
        monthName = "February"
    elif currentMonth == 3:
        monthName = "May"
    elif currentMonth == 4:
        monthName = "April"
    elif currentMonth == 5:
        monthName = "May"
    elif currentMonth == 6:
        monthName = "June"
    elif currentMonth == 7:
        monthName = "July"
    elif currentMonth == 8:
        monthName = "August"
    elif currentMonth == 9:
        monthName = "September"
    elif currentMonth == 10:
        monthName = "October"
    elif currentMonth == 11:
        monthName = "November"
    elif currentMonth == 12:
        monthName = "December"
    return monthName


main()
