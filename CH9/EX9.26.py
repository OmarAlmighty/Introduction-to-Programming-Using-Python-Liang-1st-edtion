# 9.26 (Display balls with random colors) Write a program that displays ten balls with
# random colors and placed at random locations, at shown in Figure 9.36c.

from tkinter import *  # Import tkinter
from random import randint

width = 300
height = 150
radius = 4


# Convert an integer to a single hex digit in a character
def toHexChar(hexValue):
    if hexValue <= 9 and hexValue >= 0:
        return chr(hexValue + ord('0'))
    else:  # hexValue <= 15 && hexValue >= 10
        return chr(hexValue - 10 + ord('A'))


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Random Balls")  # Set title

        x = 100
        y = 100

        self.canvas = Canvas(window, width=width, height=height)
        self.canvas.pack()
        Button(window, text="Display", command=self.display).pack()

        window.mainloop()  # Create an event loop

    def display(self):
        self.canvas.delete("ball")
        for i in range(10):
            x = randint(0, width - 1)
            y = randint(0, height - 1)
            color = "#"
            for j in range(6):
                color += toHexChar(randint(0, 15))

            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, tags="ball")


MainGUI()
