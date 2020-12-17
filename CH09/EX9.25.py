# 9.25 (Traffic lights) Write a program that simulates a traffic light. The program lets the
# user select one of three lights: red, yellow, or green. When a radio button is
# selected, the light is turned on, and only one light can be on at a time (see
# Figure 9.36a–b). No light is on when the program starts.
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=250, height=290, bg='white')
        self.canvas.create_rectangle(90, 10, 165, 245)
        self.canvas.create_oval(95, 15, 160, 80, tags="r")
        self.canvas.create_oval(95, 95, 160, 160, tags="y")
        self.canvas.create_oval(95, 175, 160, 240, tags="g")
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        var = IntVar()
        Radiobutton(frame, text="Red", command=self.red, variable=var, value=1).grid(row=1, column=1)
        Radiobutton(frame, text="yellow", command=self.yellow, variable=var, value=2).grid(row=1, column=2)
        Radiobutton(frame, text="green", command=self.green, variable=var, value=3).grid(row=1, column=3)
        window.mainloop()

    def red(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(90, 10, 165, 245)
        self.canvas.create_oval(95, 15, 160, 80, tags="r", fill="red")
        self.canvas.create_oval(95, 95, 160, 160, tags="y")
        self.canvas.create_oval(95, 175, 160, 240, tags="g")

    def yellow(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(90, 10, 165, 245)
        self.canvas.create_oval(95, 15, 160, 80, tags="r")
        self.canvas.create_oval(95, 95, 160, 160, tags="y", fill="yellow")
        self.canvas.create_oval(95, 175, 160, 240, tags="g")

    def green(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(90, 10, 165, 245)
        self.canvas.create_oval(95, 15, 160, 80, tags="r")
        self.canvas.create_oval(95, 95, 160, 160, tags="y")
        self.canvas.create_oval(95, 175, 160, 240, tags="g", fill="green")


MainGUI()
