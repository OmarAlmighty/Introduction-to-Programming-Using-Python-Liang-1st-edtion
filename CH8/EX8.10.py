# 8.10 (Decimal to binary) Write a function that parses a decimal number into a binary
# number as a string. Use the function header:
# def decimalToBinary(value):
# Write a test program that prompts the user to enter a decimal integer value and displays
# the corresponding binary value.

def decimalToBinary(value):
    bin = ''
    while value > 0:
        if value % 2 == 0:
            bin = bin + '0'
        else:
            bin = bin + '1'
        value = value // 2
    bin = bin[::-1]
    return bin


def main():
    val = eval(input("Enter a decimal: "))
    bin = decimalToBinary(val)
    print(bin)


main()
