# 15.29 (Tkinter: H-tree fractal) An H-tree is a fractal defined as follows:
# 1. Begin with a letter H. The three lines of the H are of the same length, as shown
# in Figure 15.1a.
# 2. The letter H (in its sans-serif form, H) has four endpoints. Draw an H centered
# at each of the four endpoints to an H-tree of order 1, as shown in Figure 15.1b.
# These Hs are half the size of the H that contains the four endpoints.
# 3. Repeat Step 2 to create an H-tree of order 2, 3, ..., and so on, as shown in
# Figure 15.1c–d.
# Write a Python program that draws an H-tree, as shown in Figure 15.1.

import math
from tkinter import *  # Import tkinter


class H_Tree:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("H Tree")  # Set a title

        self.width = 600
        self.height = 600
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
        Button(frame1, text="Display H tree",
               command=self.display).pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def display(self):
        self.canvas.delete("line")
        length = 200
        center = [self.width / 2, self.height / 2]
        self.displayHTree(int(self.order.get()), center, length / 2)

    def displayHTree(self, order, center, length):
        if order >= 0:
            p1 = [center[0] - length / 2, center[1] + length / 2]
            p2 = [center[0] - length / 2, center[1] - length / 2]
            p3 = [center[0] + length / 2, center[1] + length / 2]
            p4 = [center[0] + length / 2, center[1] - length / 2]

            self.canvas.create_line(
                center[0] - length / 2, center[1],
                center[0] + length / 2, center[1], tags="line")
            self.canvas.create_line(
                p1[0], p1[1], p2[0], p2[1], tags="line")
            self.canvas.create_line(
                p3[0], p3[1], p4[0], p4[1], tags="line")

            # Recursively display three H shape of a smaller order
            self.displayHTree(order - 1, p1, length / 2)
            self.displayHTree(order - 1, p2, length / 2)
            self.displayHTree(order - 1, p3, length / 2)
            self.displayHTree(order - 1, p4, length / 2)


H_Tree()  # Create GUI
