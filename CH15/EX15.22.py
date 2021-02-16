# 15.22 (Hex to decimal) Write a recursive function that parses a hex number as a string
# into a decimal integer. The function header is as follows:
# def hexToDecimal(hexString):
# Write a test program that prompts the user to enter a hex string and displays its
# decimal equivalent.

hexs = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def hexToDecimal(hexString):
    return hexToDecimalHelper(hexString, 0, len(hexString) - 1)


def hexToDecimalHelper(hexString, low, high):
    if high < low:
        return 0
    else:
        if hexString[high].upper() in hexs.keys():
            dec = hexs[hexString[high].upper()]
        else:
            dec = int(hexString[high])

        return hexToDecimalHelper(hexString, low, high - 1) * 16 + dec

hex = input("Enter a hex number: ").strip()
print(hex + " is decimal " + str(hexToDecimal(hex)))