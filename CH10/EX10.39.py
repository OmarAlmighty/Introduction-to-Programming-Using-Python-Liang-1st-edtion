# 10.39 (Tkinter: the 24-point card game) The 24-point card game involves picking any four
# cards from 52 cards, as shown in Figure 10.20. Note that the jokers are excluded. Each
# card represents a number. An ace, king, queen, and jack represent 1, 13, 12, and 11,
# respectively. Enter an expression that uses the four numbers from the four selected
# cards. Each card number can be used only once in each expression, and each card
# must be used. You can use the operators ( *, and /) and parentheses in the
# expression. The expression must evaluate to 24. After entering the expression, click
# the Verify button to check whether the numbers in the expression are currently selected
# and whether the result of the expression is correct. Display the verification in a dialog
# box. You can click the Refresh button to get another set of four cards. Assume that
# images are stored in files named 1.gif, 2.gif, ..., 52.gif, in the order of spades, hearts,
# diamonds, and clubs. So, the first 13 images are for spades 1, 2, 3, ..., and 13.
import random
import tkinter.messagebox
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()

        btRefresh = Button(window, text='refresh', command=self.refresh)
        btRefresh.pack()

        self.frame = Frame(window)
        self.frame.pack()
        self.innerFrame = Frame(self.frame)
        self.innerFrame.pack()
        self.refresh()

        Label(window, text="Enter an expression: ").pack(side=LEFT)
        self.exp = StringVar()
        Entry(window, textvariable=self.exp).pack(side=LEFT)
        Button(window, text="verify", command=self.verify).pack(side=LEFT)

        window.mainloop()

    def refresh(self):
        self.innerFrame.destroy()  # delete the inner frame with its content

        self.cards = [random.randint(1, 52), random.randint(1, 52), random.randint(1, 52), random.randint(1, 52)]

        self.innerFrame = Frame(self.frame)  # create the inner frame again to add images
        self.innerFrame.pack()

        self.img1 = PhotoImage(file='card/' + str(self.cards[0]) + '.gif')
        self.img2 = PhotoImage(file='card/' + str(self.cards[1]) + '.gif')
        self.img3 = PhotoImage(file='card/' + str(self.cards[2]) + '.gif')
        self.img4 = PhotoImage(file='card/' + str(self.cards[3]) + '.gif')

        Label(self.innerFrame, image=self.img1).pack(side=LEFT)
        Label(self.innerFrame, image=self.img2).pack(side=LEFT)
        Label(self.innerFrame, image=self.img3).pack(side=LEFT)
        Label(self.innerFrame, image=self.img4).pack(side=LEFT)
        self.cards = [x % 13 for x in self.cards]  # set the values between 1 and 13

        for i in range(len(self.cards)):
            if self.cards[i] == 0:
                self.cards[i] = 13  # king
            self.cards[i] = str(self.cards[i])

    def verify(self):
        if eval(self.exp.get()) == 24.0:
            lst = self.exp.get().split()
            for x in lst:
                if x in self.cards:
                    self.cards.remove(x)

            if len(self.cards) == 0:
                tkinter.messagebox.showinfo(message="You got it")
            else:
                tkinter.messagebox.showinfo(message="You have to use 4 cards shown")
        else:
            tkinter.messagebox.showinfo(message=self.exp.get() + "is not 24")


MainGUI()
