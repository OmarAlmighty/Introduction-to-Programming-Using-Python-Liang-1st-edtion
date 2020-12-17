# 9.27 (Compare loans with various interest rates) Rewrite Exercise 5.23 to create the
# user interface shown in Figure 9.37. Your program should let the user enter the
# loan amount and loan period in the number of years from a text field, and should
# display the monthly and total payments for each interest rate starting from 5 percent
# to 8 percent, with increments of one-eighth, in a text area.
import math
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        frame = Frame(window)
        lbl1 = Label(frame, text="Loan amount: ")
        lbl2 = Label(frame, text="Number of years: ")
        self.lm = StringVar()
        self.ny = StringVar()
        ent1 = Entry(frame, textvariable=self.lm)
        ent2 = Entry(frame, textvariable=self.ny)
        lbl1.grid(row=1, column=1)
        ent1.grid(row=1, column=2)
        lbl2.grid(row=1, column=3)
        ent2.grid(row=1, column=4)
        Button(frame, text="Calculate", command=self.cal).grid(row=1, column=5)
        frame.pack()
        self.txt = Text(window)
        self.txt.pack()
        window.mainloop()

    def cal(self):
        i = int(self.ny.get())
        counter = 1
        self.txt.insert(END, "Interest Rate    Monthly Payment    Total Payment\n")
        while counter < 26:
            self.txt.insert(END, format(i, "-5.3f"))
            self.txt.insert(END, "             ")
            monthlyInterestRate = i / 1200
            monthlyPayment = int(self.lm.get()) * monthlyInterestRate / (
                        1 - 1 / math.pow(1 + monthlyInterestRate, int(self.ny.get()) * 12))
            self.txt.insert(END, format(monthlyPayment, "-5.2f"))
            self.txt.insert(END, format((monthlyPayment * 12) * int(self.ny.get()), "-24.2f"))
            self.txt.insert(END,"\n")
            counter += 1
            i += .125


MainGUI()
