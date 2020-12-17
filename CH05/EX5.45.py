# 5.45 (Decimal to hex) Write a program that prompts the user to enter a decimal integer
# and displays its corresponding hexadecimal value.

d = int(input("Enter an integer: "))

hex = ""
value = d

while value != 0:
    h = value % 16
    if h >= 10:
        hex += chr(h + 55)
    else:
        hex += str(h)

    value //= 16

res = ""
for i in range(len(hex) - 1, -1, -1):
    res += hex[i]

print("The hexadecimal representation of", d, "is", res)
