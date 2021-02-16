# 15.33 (Tkinter: Hilbert curve) The Hilbert curve, first described by German mathematician
# David Hilbert in 1891, is a space-filling curve that visits every point in
# a square grid with a size of or any other power
# of 2. Write a program that displays a Hilbert curve for the specified order, as
# shown in Figure 15.19.

import math
from tkinter import *  # Import tkinter


# NOT SOLVED :((( #


class HilbertCurve:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Hilbert curve")  # Set a title

        self.width = 600
        self.height = 600
        self.length = 400
        self.canvas = Canvas(window,
                             width=self.width, height=self.height)
        self.canvas.pack()

        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window)  # Create and add a frame to window
        frame1.pack()

        Label(frame1,
              text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()

        entry = Entry(frame1, textvariable=self.order,
                      justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display Hilbert curve",
               command=self.display).pack(side=LEFT)
        window.mainloop()  # Create an event loop

    def display(self):
        self.canvas.delete("line")

        for i in range(int(self.order.get())):
            self.length = self.length / 2  # Get the right length for the order

        # Get the start point
        x = self.width / 2 + self.length / 2
        y = self.height / 2 - self.length / 2

        self.upperU(x, y, int(self.order.get()))

    def upperU(self, x, y, order):
        if order > 0:
            self.leftU(x, y, order - 1)
            x, y = self.drawLine(x, y, 270)
            self.upperU(x, y, order - 1)
            x, y = self.drawLine(x, y, 0)
            self.upperU(x, y, order - 1)
            x, y = self.drawLine(x, y, 90)
            self.rightU(x, y, order - 1)

    def leftU(self, x, y, order):
        if order > 0:
            self.upperU(x, y, order - 1)
            x, y = self.drawLine(x, y,0)
            self.leftU(x, y, order - 1)
            x, y = self.drawLine(x, y, 270)
            self.leftU(x, y, order - 1)
            x, y = self.drawLine(x, y, 180)
            self.downU(x, y, order - 1)

    def rightU(self, x, y, order):
        if order > 0:
            self.downU(x, y, order - 1)
            x, y = self.drawLine(x, y, 180)
            self.rightU(x, y, order - 1)
            x, y = self.drawLine(x, y, 90)
            self.rightU(x, y, order - 1)
            x, y = self.drawLine(x, y, 0)
            self.upperU(x, y, order - 1)

    def downU(self, x, y, order):
        if order > 0:
            self.rightU(x, y, order - 1)
            x, y = self.drawLine(x, y, 90)
            self.downU(x, y, order - 1)
            x, y = self.drawLine(x, y, 180)
            self.downU(x, y, order - 1)
            x, y = self.drawLine(x, y, 270)
            self.leftU(x, y, order - 1)

    def drawLine(self, x, y, angle):
        angle = angle * math.pi / 180
        x2 = x + self.length * math.sin(angle)
        y2 = y + self.length * math.cos(angle)
        self.canvas.create_line(x, y, x2, y2, tag="line")
        return x2, y2


HilbertCurve()  # Create GUI
