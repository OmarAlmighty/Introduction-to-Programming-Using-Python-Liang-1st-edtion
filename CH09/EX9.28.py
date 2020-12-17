# 9.28 (Geometry: display angles) Write a program that enables the user to drag the vertices
# of a triangle and displays the angles dynamically, as shown in Figure 9.38a.
# Change the mouse cursor to the cross-hair shape when the mouse is moved close
# to a vertex. The formula to compute angles A, B, and C (see Figure 9.38b) is given
# in Listing 3.2.
# Hint: Use the Point class to represent a point, as described in Exercise 8.17. Create
# three points at random locations initially. When the mouse is moved close to a
# point, change the cursor to a cross-hair pointer and reset the point to where the
# mouse is. Whenever a point is moved, redisplay the triangle and the angles.

from tkinter import *  # Import tkinter
from random import randint
import math

width = 300
height = 200
radius = 2


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Is point (x, y) close to this point
    def isNearBy(self, x, y):
        return distance(self.x, self.y, x, y) < radius + 3


def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Triangle angles")  # Set title

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()

        self.p1 = Point(randint(0, width - 1), randint(0, height - 1))
        self.p2 = Point(randint(0, width - 1), randint(0, height - 1))
        self.p3 = Point(randint(0, width - 1), randint(0, height - 1))
        self.drawTriangle()

        self.canvas.bind("<B1-Motion>", self.mouseMoved)

        window.mainloop()  # Create an event loop

    def mouseMoved(self, event):
        if self.closeToAPoint(event.x, event.y):
            self.canvas["cursor"] = "plus"
        else:
            self.canvas["cursor"] = "arrow"

        if self.p1.isNearBy(event.x, event.y):
            self.p1.x = event.x
            self.p1.y = event.y
        elif self.p2.isNearBy(event.x, event.y):
            self.p2.x = event.x
            self.p2.y = event.y
        elif self.p3.isNearBy(event.x, event.y):
            self.p3.x = event.x
            self.p3.y = event.y

        self.drawTriangle()

    def closeToAPoint(self, x, y):
        return self.p1.isNearBy(x, y) or self.p2.isNearBy(x, y) or self.p3.isNearBy(x, y)

    def drawTriangle(self):
        self.canvas.delete("line")
        self.canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, tags="line")
        self.canvas.create_line(self.p2.x, self.p2.y, self.p3.x, self.p3.y, tags="line")
        self.canvas.create_line(self.p3.x, self.p3.y, self.p1.x, self.p1.y, tags="line")

        a = distance(self.p2.x, self.p2.y, self.p3.x, self.p3.y)
        b = distance(self.p1.x, self.p1.y, self.p3.x, self.p3.y)
        c = distance(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        A = math.degrees(math.acos((a * a - b * b - c * c) / (-2 * b * c)))
        B = math.degrees(math.acos((b * b - a * a - c * c) / (-2 * a * c)))
        C = math.degrees(math.acos((c * c - b * b - a * a) / (-2 * a * b)))

        self.canvas.create_text(self.p1.x, self.p1.y, text=str(int(A)), tags="line")
        self.canvas.create_text(self.p2.x, self.p2.y, text=str(int(B)), tags="line")
        self.canvas.create_text(self.p3.x, self.p3.y, text=str(int(C)), tags="line")


MainGUI()
