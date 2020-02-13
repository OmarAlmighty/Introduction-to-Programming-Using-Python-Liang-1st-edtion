# 9.1 (Move the ball) Write a program that moves a ball in a panel. You should define a
# panel class for displaying the ball and provide the methods for moving the ball
# left, right, up, and down, as shown in Figure 9.22a. Check the boundaries to prevent
# the ball from moving out of sight completely.
from tkinter import *


class Demo:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=500, height=500, bg="white")
        self.canvas.pack()
        self.circle = self.canvas.create_oval(100, 100, 150, 150, fill="red")
        frame = Frame(window)
        self.var = IntVar()
        lBtn = Button(frame, text="Left", command=self.moveLeft).grid(row=1, column=1)
        rBtn = Button(frame, text="right", command=self.moveRight).grid(row=1, column=2)
        uBtn = Button(frame, text="up", command=self.moveUp).grid(row=1, column=3)
        dBtn = Button(frame, text="down", command=self.moveDown).grid(row=1, column=4)
        frame.pack()

        window.mainloop()

    def moveLeft(self):
        x1, y1, x2, y2 = self.canvas.coords(self.circle)
        if x1 > 0:
            self.canvas.move(self.circle, -5, 0)

    def moveRight(self):
        x1, y1, x2, y2 = self.canvas.coords(self.circle)
        if x1 < 450:
            self.canvas.move(self.circle, 5, 0)

    def moveUp(self):
        x1, y1, x2, y2 = self.canvas.coords(self.circle)
        if y1 > 0:
            self.canvas.move(self.circle, 0, -5)

    def moveDown(self):
        x1, y1, x2, y2 = self.canvas.coords(self.circle)
        if y1 < 450:
            self.canvas.move(self.circle, 0, 5)


Demo()
