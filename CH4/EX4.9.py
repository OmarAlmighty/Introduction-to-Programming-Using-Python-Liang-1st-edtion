# (Financial: compare costs) Suppose you shop for rice and find it in two differentsized
# packages. You would like to write a program to compare the costs of the
# packages. The program prompts the user to enter the weight and price of each
# package and then displays the one with the better price.

w1, p1 = eval(input("Enter weight and price for package 1: "))
w2, p2 = eval(input("Enter weight and price for package 2: "))

pricePerKilo1 = p1 / w1
pricePerKilo2 = p2 / w2

if pricePerKilo1 > pricePerKilo2:
    print("Package 1 has the better price.")
elif pricePerKilo2 > pricePerKilo1:
    print("Package 2 has the better price.")
else:
    print("Both have a good price")
