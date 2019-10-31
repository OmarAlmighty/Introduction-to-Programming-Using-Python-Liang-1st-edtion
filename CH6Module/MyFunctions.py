#############################################################
# This file contains all functions required for this chapter
#############################################################


# Converts from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


# Converts from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


# Converts from feet to meters
def footToMeter(foot):
    meter = 0.305 * foot
    return meter


# Converts from meters to feet
def meterToFoot(meter):
    foot = meter / 0.305
    return foot


# Check whether number is prime
def isPrime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            # If true, number is not prime
            return False  # number is not a prime
        divisor += 1
    return True  # number is prime


def computeCommission(salesAmount):
    commission = 0
    if salesAmount > 10000:
        commission = (5000 * 0.08) + (5000 * 0.1) + (salesAmount - 10000) * 0.12
    elif salesAmount > 5000:
        commission = 5000 * 0.08 + (salesAmount - 5000) * 0.1
    else:
        commission = salesAmount * 0.08

    return commission


def computePi(i):
    sum = 0
    for j in range(1, i + 1):
        sum += ((-1) ** (j + 1)) / (2 * j - 1)

    pi = 4 * sum
    return pi


def computeTax(status, taxableIncome):
    tax = 0
    if status == 0:
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 33950:
            tax = 8350 * 0.10 + taxableIncome - 8350 * 0.15
        elif taxableIncome <= 82250:
            tax = 8350 * 0.10 + 33950 - 8350 * 0.15 + taxableIncome - 33950 * 0.25
        elif taxableIncome <= 171550:
            tax = 8350 * 0.10 + 33950 - 8350 * 0.15 + 82250 - 33950 \
                  * 0.25 + taxableIncome - 82250 * 0.28
        elif taxableIncome <= 372950:
            tax = 8350 * 0.10 + 33950 - 8350 * 0.15 + 82250 - 33950 \
                  * 0.25 + 171550 - 82250 * 0.28 + taxableIncome - 171550 * 0.33
        else:
            tax = 8350 * 0.10 + 33950 - 8350 * 0.15 + 82250 - 33950 \
                  * 0.25 + 171550 - 82250 * 0.28 + 372950 - 171550 \
                  * 0.33 + taxableIncome - 372950 * 0.35
    elif status == 1:
        if taxableIncome <= 16700:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 67900:
            tax = 16700 * 0.10 + taxableIncome - 16700 * 0.15
        elif taxableIncome <= 137050:
            tax = 16700 * 0.10 + 67900 - 16700 * 0.15 \
                  + taxableIncome - 67900 * 0.25
        elif taxableIncome <= 208850:
            tax = 16700 * 0.10 + 67900 - 16700 * 0.15 + 137050 - 67900 \
                  * 0.25 + taxableIncome - 137050 * 0.28
        elif taxableIncome <= 372950:
            tax = 16700 * 0.10 + 67900 - 16700 * 0.15 + 137050 - 67900 \
                  * 0.25 + 208850 - 137050 * 0.28 \
                  + taxableIncome - 208850 * 0.33
        else:
            tax = 16700 * 0.10 + 67900 - 16700 * 0.15 + 137050 - 67900 \
                  * 0.25 + 208850 - 137050 * 0.28 + 372950 - 208850 \
                  * 0.33 + taxableIncome - 372950 * 0.35
    elif status == 2:
        if taxableIncome <= 8350:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 33950:
            tax = 8350 * 0.10 + taxableIncome - 8350 * 0.15
        elif taxableIncome <= 68525:
            tax = 8350 * 0.10 + 33950 - 8350 * 0.15 \
                  + taxableIncome - 33950 * 0.25
        elif taxableIncome <= 104425:
            tax = 8350 * 0.10 + 33950 - 8350 * 0.15 + 68525 - 33950 \
                  * 0.25 + taxableIncome - 68525 * 0.28
        elif taxableIncome <= 186475:
            tax = 8350 * 0.10 + 33950 - 8350 * 0.15 + 68525 - 33950 \
                  * 0.25 + 104425 - 68525 * 0.28 \
                  + taxableIncome - 104425 * 0.33
        else:
            tax = 8350 * 0.10 + 33950 - 8350 * 0.15 + 68525 - 33950 \
                  * 0.25 + 104425 - 68525 * 0.28 + 186475 - 104425 \
                  * 0.33 + taxableIncome - 186475 * 0.35
    elif status == 3:
        if taxableIncome <= 11950:
            tax = taxableIncome * 0.10
        elif taxableIncome <= 45500:
            tax = 11950 * 0.10 + taxableIncome - 11950 * 0.15
        elif taxableIncome <= 117450:
            tax = 11950 * 0.10 + 45500 - 11950 * 0.15 \
                  + taxableIncome - 45500 * 0.25
        elif taxableIncome <= 190200:
            tax = 11950 * 0.10 + 45500 - 11950 * 0.15 + 117450 - 45500 \
                  * 0.25 + taxableIncome - 117450 * 0.28
        elif taxableIncome <= 372950:
            tax = 11950 * 0.10 + 45500 - 11950 * 0.15 + 117450 - 45500 \
                  * 0.25 + 190200 - 117450 * 0.28 \
                  + taxableIncome - 190200 * 0.33
        else:
            tax = 11950 * 0.10 + 45500 - 11950 * 0.15 + 117450 - 45500 \
                  * 0.25 + 190200 - 117450 * 0.28 + 372950 - 190200 \
                  * 0.33 + taxableIncome - 372950 * 0.35
    else:
        print("Error: invalid status")
        return 0

    return tax


def numberOfDaysInAYear(year):
    if isLeapYear(year):
        return 366
    else:
        return 365


# Determine if it is a leap year *
def isLeapYear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


# Returns true if the sum of any two sides is
# greater than the third side.
def isValid(side1, side2, side3):
    b1 = side1 + side2 > side3
    b2 = side2 + side3 > side1
    b3 = side1 + side3 > side2
    return (b1 and b2 and b3)


# Returns the area of the triangle.
def area(side1, side2, side3):
    if isValid(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        return area


# Return true if point (x2, y2) is on the left side of the
# directed line from (x0, y0) to (x1, y1)
def leftOfTheLine(x0, y0, x1, y1, x2, y2):
    d = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return d > 0


# Return true if point (x2, y2) is on the same
# line from (x0, y0) to (x1, y1)
def onTheSameLine(x0, y0, x1, y1, x2, y2):
    d = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return d == 0


# Return true if point (x2, y2) is on the
# line segment from (x0, y0) to (x1, y1)
def onTheLineSegment(x0, y0, x1, y1, x2, y2):
    d = (x1 - x0) * (y2 - y0) - (x2 - x0) * (y1 - y0)
    return d < 0


def sqrt(n):
    lastGuess = n
    init = 0.0001
    nextGuess = (lastGuess + (n / lastGuess)) / 2
    while (lastGuess - nextGuess) >= init:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2

    return nextGuess


def isPalindrome(number):
    return number == reverse(number)


# Return the reversal of an integer, i.e. reverse(456) returns 654
def reverse(number):
    result = 0
    while number != 0:
        remainder = number % 10
        result = result * 10 + remainder
        number = number // 10

    return result
