# 9.6 (Game: display a tic-tac-toe board ) Write a program that displays nine labels.
# Each label may display an image icon for an X or an image icon for an O, as
# shown in Figure 9.25b. What to display is randomly decided. Use the
# random.randint(0, 1) function to generate an integer 0 or 1, which corresponds
# to displaying a cross image (X) icon or a not image (O) icon. The cross and
# not images are in the files x.gif and o.gif.
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

window.mainloop()
