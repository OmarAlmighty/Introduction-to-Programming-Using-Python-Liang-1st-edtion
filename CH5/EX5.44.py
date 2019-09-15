# 5.44 (Decimal to binary) Write a program that prompts the user to enter a decimal integer
# and displays its corresponding binary value.

d = int(input("Enter an integer: "))

bin = ""
value = d

while value != 0:
    bin = str(value % 2) + bin
    value = value // 2

print("The binary representation of", d, "is", bin)
