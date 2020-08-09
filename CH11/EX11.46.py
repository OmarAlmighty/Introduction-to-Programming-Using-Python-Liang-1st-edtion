# 11.46 (Tkinter: display a STOP sign) Write a program that displays a STOP sign, as
# shown in Figure 11.17a. The hexagon is in red and the text is in black.

from tkinter import *  # Import tkinter
import math


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Stop Sign")  # Set title

        width = 200
        height = 150
        canvas = Canvas(window, bg="white", width=width, height=height)
        canvas.pack()

        xCenter = width / 2
        yCenter = height / 2
        radius = min(width, height) * 0.5

        # Create a Polygon object
        polygon = []

        # Add points to the polygon
        for i in range(8):
            polygon.append([xCenter + radius *
                            math.cos(i * 2 * math.pi / 8 + 2 * math.pi / 16), yCenter - radius *
                            math.sin(i * 2 * math.pi / 8 + 2 * math.pi / 16)])

        # Draw the polygon
        canvas.create_polygon(polygon, fill="red")
        canvas.create_text(xCenter, yCenter, text="STOP", font="Times 30 bold", fill="white")

        window.mainloop()  # Create an event loop


MainGUI()
