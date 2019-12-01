# 8.15 (Business: check ISBN-10) An ISBN-10 (International Standard Book Number)
# consists of 10 digits:d1d2d3d4d5d6d7d8d9d10. The last digit, is a checksum,
# which is calculated from the other nine digits using the following formula:
# (d1 * 1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5
# + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11
# If the checksum is 10, the last digit is denoted as X, according to the ISBN convention.
# Write a program that prompts the user to enter the first 9 digits as a string
# and displays the 10-digit ISBN (including leading zeros). Your program should
# read the input as a string.

digits = input("Enter the first 9 digits of an ISBN-10 as a string: ")
if digits.isdigit():
    lastDigit = 0
    for i in range(9):
        lastDigit += int(digits[i]) * (i+1)
    lastDigit = lastDigit % 11
    isbn = ''
    if lastDigit == 10:
        isbn = digits + 'X'
    else:
        isbn = digits + str(lastDigit)

    print("The ISBN-10 number is", isbn)
else:
    print("incorrect input")