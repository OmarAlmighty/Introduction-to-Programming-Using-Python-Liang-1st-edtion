# 15.31 (Tkinter: Recursive tree) Write a program to display a recursive tree, as shown in
# Figure 15.17.

import math
from tkinter import *  # Import tkinter


class Recursive_Tree:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Recursive tree")  # Set a title

        self.width = 600
        self.height = 600
        self.canvas = Canvas(window,
                             width=self.width, height=self.height)
        self.canvas.pack()

        # Add a label, an entry, and a button to frame1
        frame1 = Frame(window)  # Create and add a frame to window
        frame1.pack()
        self.angleFactor = math.pi / 5
        self.sizeFactor = 0.58
        Label(frame1,
              text="Enter an order: ").pack(side=LEFT)
        self.order = StringVar()

        entry = Entry(frame1, textvariable=self.order,
                      justify=RIGHT).pack(side=LEFT)
        Button(frame1, text="Display Recursive tree",
               command=self.display).pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def display(self):
        self.canvas.delete("line")
        self.displayRTree(int(self.order.get()), self.width/2, self.height-100, self.height / 3, math.pi / 2)

    def displayRTree(self, depth, x1, y1, length, angle):
        if depth >= 0:
            x2 = x1 - math.cos(angle) * length
            y2 = y1 - math.sin(angle) * length

            # Draw the line
            self.canvas.create_line(x1, y1, x2, y2, tag="line")

            # Draw the left branch
            self.displayRTree(depth - 1, x2, y2, length * self.sizeFactor, angle + self.angleFactor)
            # Draw the right branch
            self.displayRTree(depth - 1, x2, y2, length * self.sizeFactor, angle - self.angleFactor)


Recursive_Tree()  # Create GUI
