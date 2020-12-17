# 4.33 (Decimal to hex) Write a program that prompts the user to enter an integer
# between 0 and 15 and displays its corresponding hex number.

dec = int(input("Enter a decimal value (0 to 15): "))

if 0 <= dec < 10:
    print("The hex value is", dec)
elif dec == 10:
    print("The hex value is A")
elif dec == 11:
    print("The hex value is B")
elif dec == 12:
    print("The hex value is C")
elif dec == 13:
    print("The hex value is D")
elif dec == 14:
    print("The hex value is E")
elif dec == 15:
    print("The hex value is F")
else:
    print("Invalid input")
