# 9.5 (Game: display a checkerboard) Write a program that displays a checkerboard in
# which each white and black cell is a canvas with a background of black or white,
# as shown in Figure 9.25a.

from tkinter import *

window = Tk()
c = Canvas(window, width=320, height=320)
c.pack()
color = 0
x1 = y1 = 3
x2 = y2 = 43
for i in range(8):
    for j in range(8):
        if color == 0:
            c.create_rectangle(x1, y1, x2, y2, fill="white", outline="white")
            color = 1
        elif color == 1:
            c.create_rectangle(x1, y1, x2, y2, fill="black")
            color = 0
        x1 = x2
        x2 = x1 + 40
    y1 = y2
    y2 = y1 + 40
    x1 = 3
    x2 = 43
    color = 1 if color == 0 else 0

window.mainloop()
