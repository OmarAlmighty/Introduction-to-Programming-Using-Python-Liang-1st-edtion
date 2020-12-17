# 4.34 (Hex to heximal) Write a program that prompts the user to enter a hex character
# and displays its corresponding heximal integer.

hex = input("Enter a hex character: ")

if '0' <= hex <= '9':
    print("The decimal value is", hex)
elif hex.upper() == 'A':
    print("The decimal value is 10")
elif hex.upper() == 'B':
    print("The decimal value is 11")
elif hex.upper() == 'C':
    print("The decimal value is 12")
elif hex.upper() == 'D':
    print("The decimal value is 13")
elif hex.upper() == 'E':
    print("The decimal value is 14")
elif hex.upper() == 'D':
    print("The decimal value is 15")
else:
    print("Invalid input")
