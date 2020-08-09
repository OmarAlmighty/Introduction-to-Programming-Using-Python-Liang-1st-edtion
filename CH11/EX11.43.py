# 11.43 (Tkinter: plot the sine and cosine functions) Exercise 5.53 draws sine and cosine
# functions using Turtle. Rewrite the program to draw the sine and cosine functions
# using Tkinter, as shown in Figure 11.15b.
import math
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Sine Function")  # Set title

        width = 400
        height = 150
        canvas = Canvas(window, width=width, height=height)
        canvas.pack()

        # Draw sine function
        p = []
        for x in range(-175, 176):
            p.append([x + width / 2, -50 * math.sin((x / 100.0) * 2 * math.pi) + height / 2])

        for i in range(len(p) - 1):
            canvas.create_line(p[i], p[i + 1])

        p = []
        for x in range(-175, 176):
            p.append([x + width / 2, 50 * math.sin((x / 100.0) * 2 * math.pi) + height / 2])

        for i in range(len(p) - 1):
            canvas.create_line(p[i], p[i + 1], fill='blue')

        # Draw X-axis
        canvas.create_line(10, height / 2, width - 10, height / 2)
        canvas.create_text(width / 2 + 100, height / 2 + 10, text="2\u03c0")
        canvas.create_text(width / 2 - 100, height / 2 + 10, text="-2\u03c0")
        canvas.create_line(width - 10 - 10, height / 2 + 10, width - 10, height / 2)
        canvas.create_line(width - 10 - 10, height / 2 - 10, width - 10, height / 2)

        # Draw Y-axis
        canvas.create_line(width / 2, 10, width / 2, height - 10)
        canvas.create_line(width / 2, 10, width / 2 - 10, 10 + 10)
        canvas.create_line(width / 2, 10, width / 2 + 10, 10 + 10)

        window.mainloop()  # Create an event loop


MainGUI()
