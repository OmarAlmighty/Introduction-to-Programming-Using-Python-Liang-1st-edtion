# 9.15 (Display a still fan) Write a program that displays a still fan, as shown in
# Figure 9.29a.
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, bg="white", width=250, height=250)
        self.canvas.pack()
        self.canvas.create_arc(5, 60, 260, 220, start=20, extent=30, fill="red")
        self.canvas.create_arc(5, 60, 260, 220, start=100, extent=30, fill="red")
        self.canvas.create_arc(5, 60, 260, 220, start=200, extent=30, fill="red")
        self.canvas.create_arc(5, 60, 260, 220, start=280, extent=30, fill="red")

        window.mainloop()


MainGUI()
