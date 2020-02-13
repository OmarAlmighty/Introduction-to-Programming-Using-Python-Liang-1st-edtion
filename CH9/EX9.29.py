# 9.29 (Geometry: intersecting point) Write a program that displays two line segments
# with their end points and their intersecting point. Initially, the end points are at
# (20, 20) and (56, 130) for line 1 and at (100, 20) and (16, 130) for line 2. The
# user can use the mouse to drag a point and dynamically display the intersecting
# point, as shown in Figure 9.38c. (Hint: See Exercise 4.25 for finding the intersecting
# point of two unbounded lines. The hint for Exercise 9.28 applies to this exercise
# as well.)
from tkinter import *


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Is point (x, y) close to this point
    def isNearBy(self, x, y):
        return distance(self.x, self.y, x, y) < 8


def distance(x1, y1, x2, y2):
    return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5


class MainGUI:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=500, height=500, bg="white")
        self.canvas.pack()
        self.p11 = Point(20, 20)
        self.p12 = Point(56, 130)
        self.p21 = Point(100, 20)
        self.p22 = Point(16, 130)

        self.canvas.create_line(self.p11.x, self.p11.y, self.p12.x, self.p12.y, tags="l1")
        self.canvas.create_line(self.p21.x, self.p21.y, self.p22.x, self.p22.y, tags="l2")
        self.canvas.create_text(self.p11.x, self.p11.y, text="(20,20)", tags="p11")
        self.canvas.create_text(self.p12.x, self.p12.y, text="(56,130)", tags="p12")
        self.canvas.create_text(self.p21.x, self.p21.y, text="(100,20)", tags="p21")
        self.canvas.create_text(self.p22.x, self.p22.y, text="(16,130)", tags="p22")

        cramer = (self.p11.y - self.p12.y) * (self.p22.x - self.p21.x) - \
                 (self.p12.x - self.p11.x) * (self.p21.y - self.p22.y)
        a = self.p11.y - self.p12.y
        b = self.p12.x - self.p11.x
        c = self.p21.y - self.p22.y
        d = self.p22.x - self.p21.x
        e = (self.p11.y - self.p12.y) * self.p11.x + (self.p12.x - self.p11.x) * self.p11.y
        f = (self.p21.y - self.p22.y) * self.p21.x + (self.p22.x - self.p21.x) * self.p21.y
        x = (e * d - b * f) / cramer
        y = (a * f - e * c) / cramer
        intersctPont = "(" + str(format(x, "0.1f")) + "," + str(format(y, "0.1f")) + ")"
        self.canvas.create_text(x, y, text=intersctPont, tags="sec")

        self.canvas.bind("<B1-Motion>", self.mouseMoved)

        window.mainloop()

    def mouseMoved(self, event):
        if self.closeToAPoint(event.x, event.y):
            self.canvas["cursor"] = "plus"
        else:
            self.canvas["cursor"] = "arrow"

        if self.p11.isNearBy(event.x, event.y):
            self.p11.x = event.x
            self.p11.y = event.y
        elif self.p12.isNearBy(event.x, event.y):
            self.p12.x = event.x
            self.p12.y = event.y
        elif self.p21.isNearBy(event.x, event.y):
            self.p21.x = event.x
            self.p21.y = event.y
        elif self.p22.isNearBy(event.x, event.y):
            self.p22.x = event.x
            self.p22.y = event.y

        self.drawLines()

    def closeToAPoint(self, x, y):
        return self.p11.isNearBy(x, y) or self.p21.isNearBy(x, y) \
               or self.p12.isNearBy(x, y) or self.p22.isNearBy(x, y)

    def drawLines(self):
        self.canvas.delete("all")
        t1 = "(" + str(self.p11.x) + "," + str(self.p11.y) + ")"
        t2 = "(" + str(self.p12.x) + "," + str(self.p12.y) + ")"
        t3 = "(" + str(self.p21.x) + "," + str(self.p21.y) + ")"
        t4 = "(" + str(self.p22.x) + "," + str(self.p22.y) + ")"

        self.canvas.create_line(self.p11.x, self.p11.y, self.p12.x, self.p12.y, tags="l1")
        self.canvas.create_line(self.p21.x, self.p21.y, self.p22.x, self.p22.y, tags="l2")
        self.canvas.create_text(self.p11.x, self.p11.y, text=t1, tags="p11")
        self.canvas.create_text(self.p12.x, self.p12.y, text=t2, tags="p12")
        self.canvas.create_text(self.p21.x, self.p21.y, text=t3, tags="p21")
        self.canvas.create_text(self.p22.x, self.p22.y, text=t4, tags="p22")

        cramer = (self.p11.y - self.p12.y) * (self.p22.x - self.p21.x) - \
                 (self.p12.x - self.p11.x) * (self.p21.y - self.p22.y)
        a = self.p11.y - self.p12.y
        b = self.p12.x - self.p11.x
        c = self.p21.y - self.p22.y
        d = self.p22.x - self.p21.x
        e = (self.p11.y - self.p12.y) * self.p11.x + (self.p12.x - self.p11.x) * self.p11.y
        f = (self.p21.y - self.p22.y) * self.p21.x + (self.p22.x - self.p21.x) * self.p21.y
        x = (e * d - b * f) / cramer
        y = (a * f - e * c) / cramer
        intersctPont = "(" + str(format(x, "0.1f")) + "," + str(format(y, "0.1f")) + ")"
        self.canvas.create_text(x, y, text=intersctPont, tags="sec")


MainGUI()
