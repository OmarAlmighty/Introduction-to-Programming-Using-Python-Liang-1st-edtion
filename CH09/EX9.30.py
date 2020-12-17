# 9.30 (Display a rectanguloid) Write a program that displays a rectanguloid, as shown
# in Figure 9.39a.

from tkinter import *  # Import tkinter


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Rectanguloid")  # Set title

        width = 200
        height = 150
        canvas = Canvas(window, bg="white", width=width, height=height)
        canvas.pack()

        width = width * 0.9 - 30
        height = height * 0.9 - 60

        diff = min(width, height) * 0.4

        # Draw the front rect
        canvas.create_rectangle(10, 60, 10 + width, 60 + height)

        # Draw the back rect
        canvas.create_rectangle(30, 60 - diff, 30 + width, 60 - diff + height)

        # Connect the corners
        canvas.create_line(10, 60, 30, 60 - diff)
        canvas.create_line(10, 60 + height, 30, 60 - diff + height)
        canvas.create_line(10 + width, 60, 30 + width, 60 - diff)
        canvas.create_line(10 + width, 60 + height, 30 + width, 60 - diff + height)

        window.mainloop()  # Create an event loop


MainGUI()