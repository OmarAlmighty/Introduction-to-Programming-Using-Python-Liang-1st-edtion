# 9.21 (Geometry: inside a rectangle?) Write a program that draws a fixed rectangle centered
# at (100, 60) with width 100 and height 40. Whenever the mouse is moved,
# display the message indicating whether the mouse pointer is inside the rectangle,
# as shown in Figure 9.32. To detect whether the pointer is inside a rectangle, use the
# Rectangle2D class defined in Exercise 8.19.

# 9.20 (Geometry: inside a circle?) Write a program that draws a fixed circle centered at
# (100, 60) with radius 50. Whenever the mouse is moved while the left button is
# pressed, display the message indicating whether the mouse pointer is inside the
# circle, as shown in Figure 9.31.

from tkinter import *  # Import tkinter

width = 300
height = 300


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()
        self.canvas.create_rectangle(100, 100, 250, 150, tags="rec")

        self.canvas.bind("<B1-Motion>", self.isInside)

        window.mainloop()  # Create an event loop

    def isInside(self, event):
        self.canvas.delete("text")
        if isInsideRec(event.x, event.y):
            self.canvas.create_text(event.x, event.y - 5,
                                    text="Mouse pointer is in the rectangle", tags="text")
        else:
            self.canvas.create_text(event.x, event.y - 5,
                                    text="Mouse pointer is not in the rectangle", tags="text")


def isInsideRec(x, y):
    if x > 250 or x<100 or y < 100 or y >150:
        return False
    else:
        return True


MainGUI()

