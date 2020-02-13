# 9.31 (Display five filled circles) Write a program that displays five filled circles, as
# shown in Figure 9.39b. Enable the user to drag the blue circle using the mouse, as
# shown in Figure 9.39c.
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=350, height=250, bg="white")
        self.canvas.pack()
        self.x1 = 50;
        self.y1 = 50;
        self.x2 = 130;
        self.y2 = 130
        self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="blue", tags="c")
        self.canvas.create_oval(150, 50, 230, 130, fill="black")
        self.canvas.create_oval(250, 50, 330, 130, fill="yellow")
        self.canvas.create_oval(100, 100, 180, 180, fill="white")
        self.canvas.create_oval(200, 100, 280, 180, fill="orange")

        self.canvas.bind("<B1-Motion>", self.move)

        window.mainloop()

    def move(self, event):
        if self.insideCircle(event.x, event.y):
            self.canvas["cursor"] = "plus"
            self.canvas.delete("c")
            self.x1 = event.x -50
            self.y1 = event.y -50
            self.x2 = self.x1 + 80
            self.y2 = self.y1 + 80
            self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill="blue", tags="c")
        else:
            self.canvas["cursor"] = "arrow"


    def insideCircle(self, x, y):
        a = (self.x1 + self.x2) / 2
        b = (self.y1 + self.y2) / 2
        return (((a - x) * (a - x) + (b - y) * (b - y)) ** 0.5) < 40


MainGUI()
