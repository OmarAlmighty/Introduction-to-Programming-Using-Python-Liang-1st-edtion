# 5.24 (Financial application: loan amortization schedule) The monthly payment for a
# given loan pays the principal and the interest. The monthly interest is computed by
# multiplying the monthly interest rate and the balance (the remaining principal).
# The principal paid for the month is therefore the monthly payment minus the
# monthly interest. Write a program that lets the user enter the loan amount, number
# of years, and interest rate, and then displays the amortization schedule for the loan.


loanAmount = eval(input("Loan amount: "))
numOfYears = eval(input("Number of years: "))
annualIR = eval(input("Annual Interest Rate: "))
print()
monthlyIR = annualIR / 1200

monthlyPayment = loanAmount * monthlyIR / (1 - (pow(1 / (1 + monthlyIR), numOfYears * 12)))

balance = loanAmount
print("Monthly Payment:", int(monthlyPayment * 100) / 100.0)
print("Total Payment:", int(monthlyPayment * 12 * numOfYears * 100) / 100.0)
print()
print(format("Payment#", "<15s"), format("Interest", "<15s"), format("Principal", "<15s"), format("Balance", "<15s"))

for i in range(1, numOfYears * 12 + 1):
    interest = int(monthlyIR * balance * 100) / 100.0
    principal = int((monthlyPayment - interest) * 100) / 100.0
    balance = int((balance - principal) * 100) / 100.0
    print(format(i, "<15d"), format(interest, "<15.2f"), format(principal, "<15.2f"), format(balance, "<15.2f"))