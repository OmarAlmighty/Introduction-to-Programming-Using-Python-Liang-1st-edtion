# 9.12 (Alternate two messages) Write a program to change, with a left mouse click,
# between two messages displayed on a canvas, “Programming is fun” and “It is fun
# to program,” as shown in Figure 9.27b–c.
from tkinter import *  # Import tkinter

width = 220
height = 100


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Rotating Message")  # Set a title

        self.on = False
        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()
        self.canvas.create_text(width / 2, height / 2, text="Programming is fun", tags="text")

        # Bind canvas with mouse events
        self.canvas.bind("<Button-1>", self.rotate)

        window.mainloop()  # Create an event loop

    def rotate(self, event):
        self.canvas.delete("text")
        if self.on:
            self.canvas.create_text(width / 2, height / 2, text="Programming is fun", tags="text")
        else:
            self.canvas.create_text(width / 2, height / 2, text="It is fun to program", tags="text")

        self.on = not self.on


MainGUI()
