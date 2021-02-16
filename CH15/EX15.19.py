# 15.19 (Decimal to binary) Write a recursive function that converts a decimal number
# into a binary number as a string. The function header is as follows:
# def decimalToBinary(value):
# Write a test program that prompts the user to enter a decimal number and displays
# its binary equivalent.

bin = ''


def decimalToBinary(value):
    global bin
    if value != 0:
        bin = str(value % 2) + bin
        value //= 2
        decimalToBinary(value)
    return bin

d = int(input("Enter an integer: "))
print("The binary representation of", d, "is", decimalToBinary(d))
