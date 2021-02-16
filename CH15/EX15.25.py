# 15.25 (Tkinter: Koch snowflake fractal ) Section 15.8 presented the Sierpinski triangle
# fractal. In this exercise, you will write a program to display another fractal,
# called the Koch snowflake, named after a famous Swedish mathematician. A
# Koch snowflake is created as follows:
# 1. Begin with an equilateral triangle, which is considered to be the Koch fractal
# of order (or level) 0, as shown in Figure 15.14a.
# 2. Divide each line in the shape into three equal line segments and draw an outward
# equilateral triangle with the middle line segment as the base to create a
# Koch fractal of order 1, as shown in Figure 15.14b.
# 3. Repeat Step 2 to create a Koch fractal of order 2, 3, ..., and so on, as shown in
# Figure 15.14c–d.
import math
from tkinter import *  # Import tkinter


class KochSnowFlake:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Koch SnowFlake")  # Set a title

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
        Button(frame1, text="Display Koch SnowFlake",
               command=self.display).pack(side=LEFT)

        window.mainloop()  # Create an event loop

    def display(self):
        self.canvas.delete("line")
        # p1 = [self.width / 2, 100]
        # p2 = [100, self.height - 100]
        # p3 = [self.width - 100, self.height - 100]
        p1 = [self.width / 2, self.height-165]
        p2 = [100, 160]
        p3 = [self.width-100, 160]
        self.displayKochSnowFlake(int(self.order.get()), p1, p2)
        self.displayKochSnowFlake(int(self.order.get()), p2, p3)
        self.displayKochSnowFlake(int(self.order.get()), p3, p1)

    def displayKochSnowFlake(self, order, p1, p2):
        if order == 0:  # Base condition
            # Draw a triangle to connect three points
            self.canvas.create_line(
                p1[0], p1[1], p2[0], p2[1], tags="line")
        else:
            # Get points x, y, z on the edge
            deltaX = p2[0] - p1[0]
            deltaY = p2[1] - p1[1]

            x = [p1[0] + deltaX / 3, p1[1] + deltaY / 3]
            y = [p1[0] + deltaX * 2 / 3, p1[1] + deltaY * 2 / 3]
            z = [((p1[0] + p2[0]) / 2 - math.cos(math.radians(30)) * (p1[1] - p2[1]) / 3),
                 (int)((p1[1] + p2[1]) / 2 - math.cos(math.radians(30)) * (p2[0] - p1[0]) / 3)]

            # Recursively display snow flakes on lines
            self.displayKochSnowFlake(order - 1, p1, x)
            self.displayKochSnowFlake(order - 1, x, z)
            self.displayKochSnowFlake(order - 1, z, y)
            self.displayKochSnowFlake(order - 1, y, p2)



KochSnowFlake()  # Create GUI
