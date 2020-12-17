# 8.3 (Check password) Some Web sites impose certain rules for passwords. Write a
# function that checks whether a string is a valid password. Suppose the password
# rules are as follows:
# ■ A password must have at least eight characters.
# ■ A password must consist of only letters and digits.
# ■ A password must contain at least two digits.
# Write a program that prompts the user to enter a password and displays valid
# password if the rules are followed or invalid password otherwise.

digitNum = 0
charNum = 0
password = input("Enter a password: ")
for c in password[:]:
    if c.isdigit():
        digitNum += 1
    elif c.isalpha():
        charNum += 1
    else:
        print("Invalid password!")
        exit()
        break
if digitNum >= 2 and charNum >= 8:
    print("Valid password")
else:
    print("Invalid password!")