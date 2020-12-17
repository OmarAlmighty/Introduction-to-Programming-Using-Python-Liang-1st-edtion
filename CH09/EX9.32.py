# 9.32 (Two movable vertices and their distances) Write a program that displays two circles
# with radius 20 at locations (20, 20) and (120, 50) with a line connecting the
# two circles, as shown in Figure 9.40a. The distance between the circles is displayed
# along the line. The user can drag a circle. When that happens, the circle and
# its line are moved and the distance between the circles is updated. Your program
# should not allow the circles to get too close. Keep them at least 70 pixels apart
# between the two circles’ centers.

from tkinter import *  # Import tkinter
import math

width = 400
height = 250
radius = 2
radius = 20


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    # Is point (x, y) inside this circle?
    def isInside(self, x, y):
        return distance(self.x, self.y, x, y) <= self.radius


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("TwoCircles")  # Set title

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        self.x = 100
        self.y = 100

        self.c1 = Circle(20, 20, radius)
        self.c2 = Circle(120, 50, radius)
        self.paint()

        self.canvas.bind("<B1-Motion>", self.mouseMoved)

        window.mainloop()  # Create an event loop

    def mouseMoved(self, event):
        if self.c1.isInside(event.x, event.y) and distance(event.x, event.y, self.c2.x, self.c2.y) > 70:
            self.c1.x = event.x
            self.c1.y = event.y
        elif self.c2.isInside(event.x, event.y) and distance(self.c1.x, self.c1.y, event.x, event.y) > 70:
            self.c2.x = event.x
            self.c2.y = event.y

        self.canvas.delete("line")
        self.paint()

    def paint(self):
        c1 = self.c1
        c2 = self.c2
        self.canvas.create_oval(c1.x - c1.radius, c1.y - c1.radius, c1.x + c1.radius, c1.y + c1.radius, fill="red",
                                activefill="gold", tags="line")
        self.canvas.create_oval(c2.x - c2.radius, c2.y - c1.radius, c2.x + c2.radius, c2.y + c2.radius, fill="red",
                                activefill="gold", tags="line")
        self.canvas.create_line(c1.x, c1.y, c2.x, c2.y, tags="line")
        self.canvas.create_text((c1.x + c2.x) / 2, (c1.y + c2.y) / 2,
                                text=str("{0:0.2f}".format(distance(c1.x, c1.y, c2.x, c2.y))), tags="line")


def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5


MainGUI()

