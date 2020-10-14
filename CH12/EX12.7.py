# 12.7 (Tkinter: two rectangles intersect?) Using the Rectangle2D class you defined in
# Exercise 8.19, write a program that enables the user to point the mouse inside a
# rectangle and drag it. As the rectangle is being dragged, the label displays whether
# two rectangles overlap, as shown in Figure 12.19.

import math
from tkinter import *


class Rectangle2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.__x__ = x
        self.__y__ = y
        self.__w__ = width
        self.__h__ = height

    def getX(self):
        return self.__x__

    def getY(self):
        return self.__y__

    def getWidth(self):
        return self.__w__

    def getHeight(self):
        return self.__h__

    def setX(self, x):
        self.__x__ = x

    def setY(self, y):
        self.__y__ = y

    def setWidth(self, width):
        self.__w__ = width

    def setHeight(self, height):
        self.__h__ = height

    def getArea(self):
        return self.__w__ * self.__h__

    def getPerimeter(self):
        return (self.__w__ + self.__h__) * 2

    def containsPoint(self, x, y):
        return abs(x - self.__x__) <= self.__w__ and abs(y - self.__y__) <= self.__h__

    def contains(self, rect):
        dis = math.sqrt((self.__x__ - rect.getX()) ** 2 + (self.__y__ - rect.getY()) ** 2)
        return True if dis + rect.getWidth() <= self.__w__ and dis + rect.getHeight() <= self.__h__ else False

    def overlaps(self, rect):
        xOvelLap = (self.getX() >= rect.getX() and self.getX() <= rect.getX() + rect.getWidth()) or \
                   (rect.getX() >= self.getX() and rect.getX() <= self.getX() + self.getWidth())
        yOverLap = (self.getY() >= rect.getY() and self.getY() <= rect.getY() + rect.getHeight()) or \
                   (rect.getY() >= self.getY() and rect.getY() <= self.getY() + self.getHeight())
        return xOvelLap and yOverLap

    def __contains__(self, rect):
        return True if rect.contains(self) else False

    def __lt__(self, rect):
        return self.__cmp__(rect) < 0

    def __le__(self, rect):
        return self.__cmp__(rect) <= 0

    def __eq__(self, rect):
        return self.__cmp__(rect) == 0

    def __ne__(self, rect):
        return self.__cmp__(rect) != 0

    def __gt__(self, rect):
        return self.__cmp__(rect) > 0

    def __ge__(self, rect):
        return self.__cmp__(rect) >= 0


def displayRectangle(r, text):
    canvas.delete(text)
    canvas.create_rectangle(r.getX(), r.getY(), r.getX() + r.getWidth(), r.getY() + r.getHeight(), tags=text)
    canvas.create_text(r.getX() + r.getWidth() / 2, r.getY() + r.getHeight() / 2, text=text, tags=text)


def mouseMoved(event):
    if r1.containsPoint(event.x, event.y):
        r1.setX(event.x)
        r1.setY(event.y)
        displayRectangle(r1, "r1")
        if r1.overlaps(r2):
            label["text"] = "Two rectangles intersect"
        else:
            label["text"] = "Two rectangles don't intersect"
    if r2.containsPoint(event.x, event.y):
        r2.setX(event.x)
        r2.setY(event.y)
        displayRectangle(r2, "r2")
        if r1.overlaps(r2):
            label["text"] = "Two rectangles intersect"
        else:
            label["text"] = "Two rectangles don't intersect"


window = Tk()  # Create a window
window.title("Two Rectangles")  # Set title

width = 500
height = 500
label = Label(window, text="Two rectangles intersect")
label.pack()
canvas = Canvas(window, width=width, height=height)
canvas.pack()

canvas.bind("<B1-Motion>", mouseMoved)
r1 = Rectangle2D(15, 20, 90, 120)
r2 = Rectangle2D(100, 50, 120, 90)
displayRectangle(r1, "r1")
displayRectangle(r2, "r2")

window.mainloop()
