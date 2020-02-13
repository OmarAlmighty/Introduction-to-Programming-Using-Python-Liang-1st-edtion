# 9.14 (Draw lines using the arrow keys) Write a program that draws line segments using
# the arrow keys. The line starts from the center of the frame and draws toward east,
# north, west, or south when the Right arrow key, Up arrow key, Left arrow key, or
# Down arrow key is clicked, as shown in Figure 9.28c.

from tkinter import *  # Import tkinter

width = 220
height = 100


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Arrow Keys")  # Set a title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        # Bind canvas with key events
        self.canvas.bind("<Up>", self.up)
        self.canvas.bind("<Down>", self.down)
        self.canvas.bind("<Left>", self.left)
        self.canvas.bind("<Right>", self.right)
        self.canvas.focus_set()

        self.x = width / 2
        self.y = height / 2

        window.mainloop()  # Create an event loop

    def up(self, event):
        self.canvas.create_line(self.x, self.y, self.x, self.y - 5, tags="line")
        self.y -= 5

    def down(self, event):
        self.canvas.create_line(self.x, self.y, self.x, self.y + 5, tags="line")
        self.y += 5

    def left(self, event):
        self.canvas.create_line(self.x, self.y, self.x - 5, self.y, tags="line")
        self.x -= 5

    def right(self, event):
        self.canvas.create_line(self.x, self.y, self.x + 5, self.y, tags="line")
        self.x += 5


MainGUI()
