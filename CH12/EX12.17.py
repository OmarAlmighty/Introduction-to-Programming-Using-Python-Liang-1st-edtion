# 12.17 (Tkinter: the 24-point card game) Enhance Exercise 10.37 to enable the computer
# to display the expression for a 24-point game solution if one exists, as
# shown in Figure 12.27. Otherwise, report that the solution does not exist.

import random
import tkinter.messagebox
from tkinter import *
import itertools


class MainGUI:
    def __init__(self):
        window = Tk()

        header = Frame(window)
        header.pack()
        btSol = Button(header, text='Find a solution', command=self.solve)
        btSol.grid(row=0, column=0)
        self.res = StringVar()
        self.solBox = Entry(header, textvariable=self.res)
        self.solBox.grid(row=0, column=1)
        btRefresh = Button(header, text='refresh', command=self.refresh)
        btRefresh.grid(row=0, column=2)

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
        lst = self.exp.get()
        print(eval(lst))
        if eval(lst) == 24.0:
            lst = re.sub(r'[^\w]', ' ', lst)
            print(lst)
            lst = lst.split()
            for x in lst:
                if x in self.cards:
                    self.cards.remove(x)

            if len(self.cards) == 0:
                tkinter.messagebox.showinfo(message="You got it")
            else:
                tkinter.messagebox.showinfo(message="You have to use 4 cards shown")
        else:
            tkinter.messagebox.showinfo(message=self.exp.get() + "is not 24")

    # This bruteforce search algorithm from https://meatfighter.com/24puzzle/
    def solve(self):
        ops = ['+', '-', '*', '/']
        nums = self.getNumericPermutations(self.cards)
        for p in ops:
            for q in ops:
                for r in ops:
                    for i in range(24):
                        a = nums[i][0]
                        b = nums[i][1]
                        c = nums[i][2]
                        d = nums[i][3]
                        self.solBox.delete(0, END)
                        if self.eval(self.eval(a, p, b), r, self.eval(c, q, d)) == 24:
                            t = "(" + str(a) + p + str(b) + ")" + r + "(" + str(c) + q + str(d) + ")"
                            self.solBox.insert(0, t)
                            return
                        elif self.eval(self.eval(self.eval(a, p, b), q, c), r, d) == 24:
                            t = "((" + str(a) + p + str(b) + ")" + q + str(c) + ")" + r + str(d)
                            self.solBox.insert(0, t)
                            return
                        elif self.eval(self.eval(a, p, self.eval(b, q, c)), r, d) == 24:
                            t = "(" + str(a) + p + "(" + str(b) + q + str(c) + ")" + r + str(d)
                            self.solBox.insert(0, t)
                            return
                        elif self.eval(a, p, self.eval(b, q, self.eval(c, r, d))) == 24:
                            t = str(a) + p + "(" + str(b) + q + "(" + str(c) + r + str(d) + "))"
                            self.solBox.insert(0, t)
                            return
                        elif self.eval(a, p, self.eval(self.eval(b, q, c), r, d)) == 24:
                            t = str(a) + p + "((" + str(b) + q + str(c) + ")" + r + str(d) + ")"
                            self.solBox.insert(0, t)
                            return
        t = "No Solution!"
        self.solBox.insert(0, t)

    def getNumericPermutations(self, lst):
        perms = list(itertools.permutations(self.cards))  # get every possible permutation
        res = []
        for i in range(len(perms)):
            res.append([])
            for j in range(len(perms[i])):
                res[i].append(int(perms[i][j]))
        return res

    def eval(self, a, op, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b != 0:
                return a / b


MainGUI()
