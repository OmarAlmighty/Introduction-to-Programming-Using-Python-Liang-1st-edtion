# 15.20 (Decimal to hex) Write a recursive function that converts a decimal number into
# a hex number as a string. The function header is as follows:
# def decimalToHex(value):
# Write a test program that prompts the user to enter a decimal number and displays
# its hex equivalent.

hex = ''


def decimalToHex(value):
    global hex
    if value != 0:
        h = value % 16
        if h >= 10:
            hex = chr(h + 55) + hex
        else:
            hex = str(h) + hex

        value //= 16
        decimalToHex(value)
    return hex


d = int(input("Enter an integer: "))
print("The hexadecimal representation of", d, "is", decimalToHex(d))
