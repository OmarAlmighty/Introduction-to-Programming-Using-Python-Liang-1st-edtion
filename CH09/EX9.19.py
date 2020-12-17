# 9.19 (Move a circle using keys) Write a program that moves a circle up, down, left, or
# right using the arrow keys, as shown in Figure 9.30c–d.
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.cavas = Canvas(window, width=500, height=500, bg="white")
        self.cavas.pack()

        self.cavas.create_oval(250, 250, 300, 300, tags="circle")
        self.cavas.focus_set()
        self.cavas.bind("<Key>", self.move)
        window.mainloop()

    def move(self,event):
        x0, y0, x1, y1 = self.cavas.coords("circle")
        if event.keysym == "Up":
            y0 -= 5
            y1 -= 5
        elif event.keysym == "Down":
            y0 += 5
            y1 += 5
        elif event.keysym == "Right":
            x0 += 5
            x1 += 5
        elif event.keysym == "Left":
            x0 -= 5
            x1 -= 5
        self.cavas.delete("circle")
        self.cavas.create_oval(x0, y0, x1, y1, tags="circle")


MainGUI()