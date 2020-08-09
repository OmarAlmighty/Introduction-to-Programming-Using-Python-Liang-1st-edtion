# 11.49 (Game: display a tic-tac-toe board) Revise Exercise 9.6 to display a new tic-tac-toe
# board with a click of the Refresh button, as shown in Figure 11.19.


import random
from tkinter import *

window = Tk()
x = PhotoImage(file="x.gif")
o = PhotoImage(file="o.gif")
for i in range(3):
    for j in range(3):
        r = random.randint(0, 1)
        if r == 0:
            Label(window, image=x).grid(row=i + 1, column=j + 1)
        elif r == 1:
            Label(window, image=o).grid(row=i + 1, column=j + 1)


def refresh():
    for i in range(3):
        for j in range(3):
            r = random.randint(0, 1)
            if r == 0:
                Label(window, image=x).grid(row=i + 1, column=j + 1)
            elif r == 1:
                Label(window, image=o).grid(row=i + 1, column=j + 1)


Button(window, text='Refresh', command=refresh).grid(row=4, column=2)

window.mainloop()
