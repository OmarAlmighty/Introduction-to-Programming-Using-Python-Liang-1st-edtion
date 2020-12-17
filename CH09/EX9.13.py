# 9.13 (Display the mouse position) Write two programs: one that displays the mouse
# position when the mouse is clicked (see Figure 9.28a–b), and the other displays
# the mouse position when the mouse button is pressed and ceases to display it when
# the mouse button is released.
from tkinter import *


class MainGUI1:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, bg="white", width=300, height=300)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.dispPos)
        window.mainloop()

    def dispPos(self, event):
        self.canvas.delete("txt")
        x = event.x
        y = event.y
        txt = "(" + str(x) + " , " + str(y) + ")"
        self.canvas.create_text(x, y, text=txt, tags="txt")


class MainGUI2:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, bg="white", width=300, height=300)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.dispPos)
        self.canvas.bind("<ButtonRelease-1>", self.deletPos)
        window.mainloop()

    def dispPos(self, event):
        x = event.x
        y = event.y
        txt = "(" + str(x) + " , " + str(y) + ")"
        self.canvas.create_text(x, y, text=txt, tags="txt")

    def deletPos(self, event):
        self.canvas.delete("txt")


MainGUI2()
