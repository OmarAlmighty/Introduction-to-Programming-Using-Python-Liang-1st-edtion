# 11.45 (Tkinter: plot the square function) Exercise 5.54 draws a square function. Rewrite the
# program to draw the square function using Tkinter, as shown in Figure 11.16b.
import math
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Square Function")  # Set title

        width = 400
        height = 300
        canvas = Canvas(window, width=width, height=height)
        canvas.pack()

        scaleFactor = 0.01
        p = []
        for x in range(-175, 176):
            p.append([x + width / 2, -1 * scaleFactor * x * x + height -50])

        for i in range(len(p) - 1):
            canvas.create_line(p[i], p[i + 1])

        # Draw X-axis
        canvas.create_line(10, height - 50, width - 10, height - 50)
        canvas.create_line(width - 10 - 10, height - 50 + 10, width - 10, height - 50)
        canvas.create_line(width - 10 - 10, height - 50 - 10, width - 10, height - 50)

        # Draw Y-axis
        canvas.create_line(width / 2, 10, width / 2, height)
        canvas.create_line(width / 2, 10, width / 2 - 10, 10 + 10)
        canvas.create_line(width / 2, 10, width / 2 + 10, 10 + 10)

        window.mainloop()  # Create an event loop


MainGUI()
