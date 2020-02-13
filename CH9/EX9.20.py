# 9.20 (Geometry: inside a circle?) Write a program that draws a fixed circle centered at
# (100, 60) with radius 50. Whenever the mouse is moved while the left button is
# pressed, display the message indicating whether the mouse pointer is inside the
# circle, as shown in Figure 9.31.

from tkinter import *  # Import tkinter

width = 240
height = 120


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Inside the circle?")  # Set a title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()
        self.canvas.create_oval(100 - 50, 60 - 50, 100 + 50, 60 + 50, tags="circle")

        self.canvas.bind("<B1-Motion>", self.isInside)

        window.mainloop()  # Create an event loop

    def isInside(self, event):
        self.canvas.delete("text")
        if isInsideCircle(100, 60, 50, event.x, event.y):
            self.canvas.create_text(event.x, event.y - 5,
                                    text="Mouse pointer is in the circle", tags="text")
        else:
            self.canvas.create_text(event.x, event.y - 5,
                                    text="Mouse pointer is not in the circle", tags="text")


def isInsideCircle(xCenter, yCenter, radius, x, y):
    return distance(xCenter, yCenter, x, y) <= radius


def distance(xCenter, yCenter, x, y):
    return ((xCenter - x) * (xCenter - x) + (yCenter - y) * (yCenter - y)) ** 0.5;


MainGUI()