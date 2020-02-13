# 9.2 (Create an investment-value calculator) Write a program that calculates the future
# value of an investment at a given interest rate for a specified number of years. The
# formula for the calculation is as follows:
# futureValue = investmentAmount * (1 + monthlyInterestRate)years * 12
# Use text fields for users to enter the investment amount, years, and interest rate.
# Display the future amount in a text field when the user clicks the Calculate button,
# as shown in Figure 9.22b.

from tkinter import *


class Demo:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Investment Calculator")  # Set title

        Label(window, text="Investment Amount").grid(row=1, column=1, sticky=W)
        Label(window, text="Years").grid(row=2, column=1, sticky=W)
        Label(window, text="Annual Interest Rate").grid(row=3, column=1, sticky=W)
        Label(window, text="Future Value").grid(row=4, column=1, sticky=W)

        self.investmentAmount = StringVar()
        Entry(window, textvariable=self.investmentAmount, justify=RIGHT).grid(row=1, column=2)
        self.annualIR = StringVar()
        Entry(window, textvariable=self.annualIR, justify=RIGHT).grid(row=3, column=2)
        self.numberOfYears = StringVar()
        Entry(window, textvariable=self.numberOfYears, justify=RIGHT).grid(row=2, column=2)
        self.futureValue = StringVar()
        Label(window, textvariable=
        self.futureValue).grid(row=4, column=2, sticky=E)

        Button(window, text="Calculate", command=self.compute).grid(row=6, column=2, sticky=E)

        window.mainloop()

    def compute(self):
        monthlyIR = float(self.annualIR.get()) / 1200
        f = float(self.investmentAmount.get()) * \
            (1 + monthlyIR) ** (float(self.numberOfYears.get()) * 12)
        self.futureValue.set("{0:10.2f}".format(f))


Demo()
