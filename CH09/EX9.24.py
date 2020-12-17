# 9.24 (Display circles) Write a program that displays a new larger circle with a left
# mouse click and removes the largest circle with a right mouse click, as shown in
# Figure 9.35.

from tkinter import *  # Import tkinter

width = 200
height = 200


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Dynamic Circles")  # Set title

        self.radius = 20

        self.tagNumber = 0
        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.create_oval(width / 2 - self.radius, height / 2 - self.radius,
                                width / 2 + self.radius, height / 2 + self.radius, tags=str(self.tagNumber))
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.addACircle)
        self.canvas.bind("<Button-3>", self.removeACircle)

        window.mainloop()  # Create an event loop

    def addACircle(self, event):
        self.tagNumber += 1
        self.radius += 5
        self.canvas.create_oval(width / 2 - self.radius, height / 2 - self.radius,
                                width / 2 + self.radius, height / 2 + self.radius, tags=str(self.tagNumber))

    def removeACircle(self, event):
        self.canvas.delete(str(self.tagNumber))
        self.radius -= 5
        self.tagNumber -= 1


MainGUI()
