# 12.21 (Tkinter: display an n-sided regular polygon) In Exercise 12.20 you created the
# RegularPolygonCanvas subclass for displaying an n-sided regular polygon.
# Write a program that displays a regular polygon and uses two buttons named +1
# and -1 to increase or decrease the size of the polygon, as shown in Figure
# 12.31a–b. Also enable the user to increase or decrease the size by clicking the
# right or left mouse button and by pressing the UP and DOWN arrow keys.
import math
from tkinter import *


class RegularPolygonCanvas(Canvas):
    def __init__(self, parent, numberOfSides=4, width=200, height=200):
        super().__init__(parent, width=width, height=height)
        self.setNumberOfSides(numberOfSides)

    def getNumberOfSides(self):
        return self.__numberOfSides

    def setNumberOfSides(self, numberOfSides):
        self.__numberOfSides = numberOfSides
        self.drawPolygon()

    def drawPolygon(self):
        self.delete("polygon")

        width = int(self["width"])
        height = int(self["height"])
        xCenter = width / 2
        yCenter = height / 2;
        radius = min(width, height) * 0.4

        angle = 2 * math.pi / self.__numberOfSides

        # Create a Polygon object
        polygon = []

        # Add points to the polygon
        for i in range(self.__numberOfSides):
            polygon.append([xCenter + radius * math.cos(i * angle),
                            yCenter - radius * math.sin(i * angle)])

            # Draw the polygon
        self.create_polygon(polygon, fill="green", tags="polygon")

    def reDraw(self, sides):
        self.__numberOfSides = sides
        self.drawPolygon()


class MainClass:
    def __init__(self):
        self.window = Tk()  # Create a window
        self.window.title("Regular Polygons")  # Set title
        self.sides = 3
        self.canvas = RegularPolygonCanvas(self.window, self.sides)
        self.canvas.pack()

        frame = Frame(self.window)
        frame.pack()
        inc = Button(frame, text='+1', command=self.increase)
        dec = Button(frame, text='-1', command=self.decrease)
        self.canvas.bind("<Button-1>", self.clickIncrease)
        self.canvas.bind("<Button-3>", self.clickDecrease)
        self.canvas.bind("<Up>", self.clickIncrease)
        self.canvas.bind("<Down>", self.clickDecrease)
        self.canvas.focus_set()
        inc.grid(row=1, column=1)
        dec.grid(row=1, column=2)

        self.window.mainloop()  # Create an event loop

    def increase(self):
        self.sides += 1
        self.canvas.reDraw(self.sides)

    def decrease(self):
        self.sides -= 1
        self.canvas.reDraw(self.sides)

    def clickIncrease(self,event):
        self.increase()

    def clickDecrease(self,event):
        self.decrease()



MainClass()
