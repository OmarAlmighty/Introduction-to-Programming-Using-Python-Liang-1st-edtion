# 11.48 (Geometry: find the bounding rectangle) Write a program that enables the user to
# add and remove points in a two-dimensional plane dynamically, as shown in Figure
# 11.18. A minimum bounding rectangle is updated as the points are added and
# removed. Assume the radius of each point is 10 pixels.

from tkinter import *  # Import tkinter
import math

width = 500
height = 150
radius = 10


def distance(x, y, x1, y1):
    return ((x - x1) * (x - x1) + (y - y1) * (y - y1)) ** 0.5


def getBoundingRect(points):
    if len(points) < 0:
        return None

    minX = maxX = points[0][0]
    minY = maxY = points[0][1]

    for [x, y] in points:
        if x < minX:
            minX = x
        if y < minY:
            minY = y
        if x > maxX:
            maxX = x
        if y > maxY:
            maxY = y

    return minX, minY, maxX, maxY


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Bounding Rectangle")  # Set title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        # Create a 2-D list for storing points
        self.points = []

        self.displayInstructions()

        self.canvas.bind("<Button-1>", self.add)
        self.canvas.bind("<Button-3>", self.remove)

        window.mainloop()  # Create an event loop

    def add(self, event):
        self.points.append([event.x, event.y])
        self.repaint()

    def remove(self, event):
        for [x, y] in self.points:
            if distance(x, y, event.x, event.y) <= 10:
                self.points.remove([x, y])
        self.repaint()

    def repaint(self):
        self.canvas.delete("point")
        for [x, y] in self.points:
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, tags="point")

        if len(self.points) > 0:
            x1, y1, x2, y2 = getBoundingRect(self.points)
            self.canvas.create_rectangle(x1 - radius, y1 - radius, x2 + radius, y2 + radius, tags="point")

    def displayInstructions(self):
        instructions = ["INSTRUCTIONS", "Add:", "Left Click", "Remove:", "Right Click"]
        x = 20
        y = 20
        self.canvas.create_rectangle(x, y, x + 160, y + 80)
        self.canvas.create_text(x + 10 + 40, y + 20, text=instructions[0], justify=CENTER)
        for i in range(1, len(instructions), 2):
            self.canvas.create_text(x + 10 + 40, y + 20 + (i + 1) * 10, text=instructions[i], justify=RIGHT)
            self.canvas.create_text(x + 80 + 40, y + 20 + (i + 1) * 10, text=instructions[i + 1], justify=RIGHT)


MainGUI()
