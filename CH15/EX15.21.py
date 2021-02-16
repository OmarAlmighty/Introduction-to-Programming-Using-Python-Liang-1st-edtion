# 15.21 (Binary to decimal) Write a recursive function that parses a binary number as a
# string into a decimal integer. The function header is as follows:
# def binaryToDecimal(binaryString):
# Write a test program that prompts the user to enter a binary string and displays its
# decimal equivalent.


def binaryToDecimal(binaryString):
    return binaryToDecimalHelper(binaryString, 0, 0)


def binaryToDecimalHelper(str, dec, i):
    if str != '':
        dec += int(str[-1]) * 2 ** i
        return binaryToDecimalHelper(str[:len(str) - 1], dec, i + 1)

    return dec


print(binaryToDecimal(input("Enter binary string: ")))
