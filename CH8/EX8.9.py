# 8.9 (Binary to hex) Write a function that parses a binary number into a hex number.
# The function header is:
# def binaryToHex(binaryValue):
# Write a test program that prompts the user to enter a binary number and displays
# the corresponding hexadecimal value.

def binaryToHex(binaryString):
    bin = binaryString[::-1]
    hex = ''
    while len(bin) > 0:
        b = bin[0:4]
        dec = 0
        for i in range(len(b)):
            dec = dec + int(b[i]) * 2 ** i
        if 0 <= dec <= 9:
            hex += str(dec)
        elif dec == 10:
            hex += 'A'
        elif dec == 11:
            hex += 'B'
        elif dec == 12:
            hex += 'C'
        elif dec == 13:
            hex += 'D'
        elif dec == 14:
            hex += 'E'
        elif dec == 15:
            hex += 'C'
        bin = bin[4:len(bin)]
    hex = hex[::-1]
    return hex


def main():
    bin = input("Enter a binary string: ")
    hex = binaryToHex(bin)
    print(hex)


main()
