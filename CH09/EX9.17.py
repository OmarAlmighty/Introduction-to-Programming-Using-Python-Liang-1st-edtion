# 9.17 (Racing car) Write a program that simulates car racing, as shown in Figure
# 9.29b–d. The car moves from left to right. When it reaches the right end, it restarts
# from the left and continues the same process. Let the user increase and decrease
# the car’s speed by pressing the Up and Down arrow keys.
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=250, height=90, bg="white")
        self.canvas.bind("<Up>", self.incSpeed)
        self.canvas.bind("<Down>", self.decSpeed)
        self.canvas.pack()
        self.car = PhotoImage(file="car.gif")
        x = 0
        self.canvas.create_image(x, 50, image=self.car, tags="car")
        self.canvas.focus_set()
        self.dx = 10
        while True:
            self.canvas.move("car", self.dx, 0)
            self.canvas.after(100)
            self.canvas.update()
            if x < 250:
                x += self.dx
            else:
                x = 0
                self.canvas.delete("car")
                self.canvas.create_image(x, 50, image=self.car, tags="car")

        window.mainloop()

    def incSpeed(self, event):
        if self.dx < 40:
            self.dx += 5

    def decSpeed(self, event):
        if self.dx > 5:
            self.dx -= 5


MainGUI()
