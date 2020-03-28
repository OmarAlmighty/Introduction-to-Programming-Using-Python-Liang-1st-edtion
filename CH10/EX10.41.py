# 10.41 (Display five circles) Write a program that displays five circles, as shown in
# Figure 10.22a. Enable the user to drag each circle using the mouse, as shown in
# Figure 10.22b.

from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=350, height=250, bg="white")
        self.canvas.pack()

        self.loc1 = [50, 50, 130, 130]
        self.loc2 = [150, 50, 230, 130]
        self.loc3 = [250, 50, 330, 130]
        self.loc4 = [100, 100, 180, 180]
        self.loc5 = [200, 100, 280, 180]

        self.canvas.create_oval(self.loc1[0], self.loc1[1], self.loc1[2], self.loc1[3], fill="blue", tags="c1")
        self.canvas.create_oval(self.loc2[0], self.loc2[1], self.loc2[2], self.loc2[3], fill="black", tags="c2")
        self.canvas.create_oval(self.loc3[0], self.loc3[1], self.loc3[2], self.loc3[3], fill="yellow", tags="c3")
        self.canvas.create_oval(self.loc4[0], self.loc4[1], self.loc4[2], self.loc4[3], fill="white", tags="c4")
        self.canvas.create_oval(self.loc5[0], self.loc5[1], self.loc5[2], self.loc5[3], fill="orange", tags="c5")

        self.canvas.bind("<B1-Motion>", self.move)

        window.mainloop()

    def move(self, event):
        if self.insideCircle1(event.x, event.y):
            self.canvas["cursor"] = "plus"
            self.canvas.delete("c1")
            self.loc1[0] = event.x - 50
            self.loc1[1] = event.y - 50
            self.loc1[2] = self.loc1[0] + 80
            self.loc1[3] = self.loc1[1] + 80
            self.canvas.create_oval(self.loc1[0], self.loc1[1], self.loc1[2], self.loc1[3], fill="blue", tags="c1")
        elif self.insideCircle2(event.x, event.y):
            self.canvas["cursor"] = "plus"
            self.canvas.delete("c2")
            self.loc2[0] = event.x - 50
            self.loc2[1] = event.y - 50
            self.loc2[2] = self.loc2[0] + 80
            self.loc2[3] = self.loc2[1] + 80
            self.canvas.create_oval(self.loc2[0], self.loc2[1], self.loc2[2], self.loc2[3], fill="black", tags="c2")
        elif self.insideCircle3(event.x, event.y):
            self.canvas["cursor"] = "plus"
            self.canvas.delete("c3")
            self.loc3[0] = event.x - 50
            self.loc3[1] = event.y - 50
            self.loc3[2] = self.loc3[0] + 80
            self.loc3[3] = self.loc3[1] + 80
            self.canvas.create_oval(self.loc3[0], self.loc3[1], self.loc3[2], self.loc3[3], fill="yellow", tags="c3")
        elif self.insideCircle4(event.x, event.y):
            self.canvas["cursor"] = "plus"
            self.canvas.delete("c4")
            self.loc4[0] = event.x - 50
            self.loc4[1] = event.y - 50
            self.loc4[2] = self.loc4[0] + 80
            self.loc4[3] = self.loc4[1] + 80
            self.canvas.create_oval(self.loc4[0], self.loc4[1], self.loc4[2], self.loc4[3], fill="white", tags="c4")
        elif self.insideCircle5(event.x, event.y):
            self.canvas["cursor"] = "plus"
            self.canvas.delete("c5")
            self.loc5[0] = event.x - 50
            self.loc5[1] = event.y - 50
            self.loc5[2] = self.loc5[0] + 80
            self.loc5[3] = self.loc5[1] + 80
            self.canvas.create_oval(self.loc5[0], self.loc5[1], self.loc5[2], self.loc5[3], fill="orange", tags="c5")

        else:
            self.canvas["cursor"] = "arrow"

    def insideCircle1(self, x, y):
        a = (self.loc1[0] + self.loc1[2]) / 2
        b = (self.loc1[1] + self.loc1[3]) / 2
        return (((a - x) * (a - x) + (b - y) * (b - y)) ** 0.5) < 40

    def insideCircle2(self, x, y):
        a = (self.loc2[0] + self.loc2[2]) / 2
        b = (self.loc2[1] + self.loc2[3]) / 2
        return (((a - x) * (a - x) + (b - y) * (b - y)) ** 0.5) < 40

    def insideCircle3(self, x, y):
        a = (self.loc3[0] + self.loc3[2]) / 2
        b = (self.loc3[1] + self.loc3[3]) / 2
        return (((a - x) * (a - x) + (b - y) * (b - y)) ** 0.5) < 40

    def insideCircle4(self, x, y):
        a = (self.loc4[0] + self.loc4[2]) / 2
        b = (self.loc4[1] + self.loc4[3]) / 2
        return (((a - x) * (a - x) + (b - y) * (b - y)) ** 0.5) < 40

    def insideCircle5(self, x, y):
        a = (self.loc5[0] + self.loc5[2]) / 2
        b = (self.loc5[1] + self.loc5[3]) / 2
        return (((a - x) * (a - x) + (b - y) * (b - y)) ** 0.5) < 40


MainGUI()
