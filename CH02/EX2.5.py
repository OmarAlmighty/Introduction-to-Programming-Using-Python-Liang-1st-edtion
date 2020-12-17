# (Financial application: calculate tips) Write a program that reads the subtotal and
# the gratuity rate and computes the gratuity and total. For example, if the user
# enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5
# as the gratuity and 11.5 as the total.

subTotal, gratRate = eval(input("Enter the subtotal and a gratuity rate: "))
grat = subTotal * (gratRate / 100)
total = subTotal + grat
print("The gratuity is", grat, "and the total is", total)
