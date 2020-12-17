# 4.18 (Financials: currency exchange) Write a program that prompts the user to enter
# the currency exchange rate between U.S. dollars and Chinese Renminbi (RMB).
# Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for
# vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to
# convert it to Chinese RMB or U.S. dollars, respectively.

exchngRate = eval(input("Enter the exchange rate from dollars to RMB: "))
convertion = int(input("Enter 0 to convert dollars to RMB and 1 vice versa: "))
dollars = 0
rmb = 0
if convertion == 0:
    dollars = eval(input("Enter the dollar amount: "))
    rmb = dollars * exchngRate
    print("$" + format(dollars, "0.1f"), "is", format(rmb, "0.1f"), "Yuan")
elif convertion == 1:
    rmb = eval(input("Enter the RMB amount: "))
    dollars = rmb / exchngRate
    print(format(rmb, "0.1f"), "Yuan is $" + format(dollars, "0.1f"))
else:
    print("Incorrect input")