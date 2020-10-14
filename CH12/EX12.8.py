# 12.8 (Tkinter: two circles intersect?) Using the Circle2D class you defined in Exercise
# 8.18, write a program that enables the user to specify the location and size of
# two circles and displays whether the circles intersect, as shown in Figure 12.20.
# Enable the user to point the mouse inside a circle and drag it. As a circle is being
# dragged, the program updates the circle’s center coordinates and its radius in the
# text fields.
import math
from tkinter import *


class Circle2D:
    def __init__(self, x=0, y=0, radius=0):
        self.__x__ = x
        self.__y__ = y
        self.__r__ = radius

    def getX(self):
        return self.__x__

    def getY(self):
        return self.__y__

    def getRadius(self):
        return self.__r__

    def setX(self, x):
        self.__x__ = x

    def setY(self, y):
        self.__y__ = y

    def setRadius(self, radius):
        self.__r__ = radius

    def getArea(self):
        return math.pi * self.getRadius() ** 2

    def getPerimeter(self):
        return math.pi * 2 * self.getRadius()

    def containsPoint(self, x, y):
        dis = math.sqrt((self.getX() - x) ** 2 + (self.getY() - y) ** 2)
        return True if dis <= self.getRadius() else False

    def contains(self, circle):
        dis = math.sqrt((self.getX() - circle.getX()) ** 2 + (self.getY() - circle.getY()) ** 2)
        return True if self.getRadius() >= dis + circle.getRadius() else False

    def overlaps(self, circle):
        dis = math.sqrt((self.getX() - circle.getX()) ** 2 + (self.getY() - circle.getY()) ** 2)
        return True if dis <= self.getRadius() + circle.getRadius() else False

    def __contains__(self, circle):
        return circle.contains(self)

    def __eq__(self, circle):
        return True if self.getRadius() == circle.getRadius() else False

    def __ne__(self, circle):
        return True if self.getRadius() != circle.getRadius() else False

    def __cmp__(self, circle):
        if self.getRadius() > circle.getRadius():
            return 1
        elif self.getRadius() < circle.getRadius():
            return -1
        else:
            return 0

    def __lt__(self, circle):
        return self.getRadius() < circle.getRadius()

    def __gt__(self, circle):
        return self.getRadius() > circle.getRadius()

    def __ge__(self, circle):
        return self.getRadius() >= circle.getRadius()

    def __le__(self, circle):
        return self.getRadius() <= circle.getRadius()


def displayCircle(c, text):
    canvas.delete(text)
    canvas.create_oval(c.getX() - c.getRadius(),
                       c.getY() - c.getRadius(), c.getX() + c.getRadius(), c.getY() + c.getRadius(), tags=text)
    canvas.create_text(c.getX(), c.getY(), text=text, tags=text)


def mouseMoved(event):
    if c1.containsPoint(event.x, event.y):
        c1.setX(event.x)
        c1.setY(event.y)
        displayCircle(c1, "c1")
        c1x.set(c1.getX())
        c1y.set(c1.getY())
        c1Radius.set(c1.getRadius())
        if c1.overlaps(c2):
            label["text"] = "Two circles intersect"
        else:
            label["text"] = "Two circles don't intersect"
    elif c2.containsPoint(event.x, event.y):
        c2.setX(event.x)
        c2.setY(event.y)
        displayCircle(c2, "c2")
        c2x.set(c2.getX())
        c2y.set(c2.getY())
        c2Radius.set(c2.getRadius())
        if c1.overlaps(c2):
            label["text"] = "Two circles intersect"
        else:
            label["text"] = "Two circles don't intersect"


def redraw():
    c1 = Circle2D(c1x.get(), c1y.get(), c1Radius.get())
    c2 = Circle2D(c2x.get(), c2y.get(), c2Radius.get())
    displayCircle(c1, "c1")
    displayCircle(c2, "c2")


window = Tk()  # Create a window
window.title("Two Circles")  # Set title

width = 250
height = 100
label = Label(window, text="Two circles intersect")
label.pack()
canvas = Canvas(window, width=width, height=height)
canvas.pack()

canvas.bind("<B1-Motion>", mouseMoved)
c1 = Circle2D(10, 10, 30)
c2 = Circle2D(30, 40, 20)
displayCircle(c1, "c1")
displayCircle(c2, "c2")

frame1 = Frame(window)
frame1.pack()
Label(frame1, text="C1 Center x:").grid(row=1, column=1)
Label(frame1, text="C1 Center y:").grid(row=2, column=1)
Label(frame1, text="C1 Radius:").grid(row=3, column=1)

c1x = DoubleVar()
c1x.set(c1.getX())
Entry(frame1, width=5, justify=RIGHT, textvariable=c1x).grid(row=1, column=2)

c1y = DoubleVar()
c1y.set(c1.getY())
Entry(frame1, width=5, justify=RIGHT, textvariable=c1y).grid(row=2, column=2)

c1Radius = DoubleVar()
c1Radius.set(c1.getRadius())
Entry(frame1, width=5, justify=RIGHT, textvariable=c1Radius).grid(row=3, column=2)

Label(frame1, text="C2 Center x:").grid(row=1, column=3)
Label(frame1, text="C2 Center y:").grid(row=2, column=3)
Label(frame1, text="C2 Radius:").grid(row=3, column=3)

c2x = DoubleVar()
c2x.set(c2.getX())
Entry(frame1, width=5, justify=RIGHT, textvariable=c2x).grid(row=1, column=4)

c2y = DoubleVar()
c2y.set(c2.getY())
Entry(frame1, width=5, justify=RIGHT, textvariable=c2y).grid(row=2, column=4)

c2Radius = DoubleVar()
c2Radius.set(c2.getRadius())
Entry(frame1, width=5, justify=RIGHT, textvariable=c2Radius).grid(row=3, column=4)

frame2 = Frame(window)
frame2.pack()
Button(frame2, text="Redraw Circles", command=redraw).pack()

window.mainloop()  # Create an event loop
