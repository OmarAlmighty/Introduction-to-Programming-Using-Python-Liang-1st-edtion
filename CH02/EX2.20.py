# (Financial application: calculate interest) If you know the balance and the annual
# percentage interest rate, you can compute the interest on the next monthly payment
# using the following formula:
# interest = balance * (annualInterestRate / 1200)
# Write a program that reads the balance and the annual percentage interest rate
# and displays the interest for the next month.

balance, ir = eval(input("Enter balance and interest rate (e.g., 3 for 3%):"))
intreset = balance * (ir / 1200)
print("The interest is", intreset)
