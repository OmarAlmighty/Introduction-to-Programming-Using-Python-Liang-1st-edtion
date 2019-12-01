# 8.8 (Binary to decimal) Write a function that parses a binary number as a string into a
# decimal integer. Use the function header:
# def binaryToDecimal(binaryString):
# For example, binary string 10001 is 17
# So, binaryToDecimal("10001") returns 17.
# Write a test program that prompts the user to enter a binary string and displays the
# corresponding decimal integer value.

def binaryToDecimal(binaryString):
    bin = binaryString[::-1]
    dec = 0
    for i in range(len(bin)):
        dec = dec + int(bin[i]) * 2 ** i
    return dec


def main():
    bin = input("Enter binary string: ")
    dec = binaryToDecimal(bin)
    print(dec)


main()
