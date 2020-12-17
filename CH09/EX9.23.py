# 9.23 (Buttons and radio buttons) Write a program that uses radio buttons to select background
# colors for text, as shown in Figure 9.34. The available colors are red, yellow,
# white, gray, and green. The program uses the buttons and to move
# the text left or right.
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        menuBar = Menu(window)
        window.config(menu=menuBar)
        menuBar.add_radiobutton(label="red", command=self.red)
        menuBar.add_radiobutton(label="yellow", command=self.yellow)
        menuBar.add_radiobutton(label="white", command=self.white)
        menuBar.add_radiobutton(label="gray", command=self.gray)
        menuBar.add_radiobutton(label="green", command=self.green)
        self.canvas = Canvas(window, width=250, height=50, bg="white")
        self.x = 35
        self.color = "white"
        self.txt = self.canvas.create_text(self.x, 25, text="Welcome", tags="txt")
        self.b = self.canvas.create_rectangle(self.canvas.bbox(self.txt), fill=self.color)
        self.canvas.tag_lower(self.b, self.txt)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        btnR = Button(frame, text="<=", command=self.right)
        btnR.grid(row=1, column=1)
        btnL = Button(frame, text="=>", command=self.left)
        btnL.grid(row=1, column=2)
        window.mainloop()

    def red(self):
        self.canvas.delete("all")
        self.color = "red"
        self.txt = self.canvas.create_text(self.x, 25, text="Welcome", tags="txt")
        self.b = self.canvas.create_rectangle(self.canvas.bbox(self.txt), fill=self.color, tags="rec")
        self.canvas.tag_lower(self.b, self.txt)

    def green(self):
        self.canvas.delete("all")
        self.color = "green"
        self.txt = self.canvas.create_text(self.x, 25, text="Welcome", tags="txt")
        self.b = self.canvas.create_rectangle(self.canvas.bbox(self.txt), fill=self.color, tags="rec")
        self.canvas.tag_lower(self.b, self.txt)

    def white(self):
        self.canvas.delete("all")
        self.color = "white"
        self.txt = self.canvas.create_text(self.x, 25, text="Welcome", tags="txt")
        self.b = self.canvas.create_rectangle(self.canvas.bbox(self.txt), fill=self.color, tags="rec")
        self.canvas.tag_lower(self.b, self.txt)

    def yellow(self):
        self.canvas.delete("all")
        self.color = "yellow"
        self.txt = self.canvas.create_text(self.x, 25, text="Welcome", tags="txt")
        self.b = self.canvas.create_rectangle(self.canvas.bbox(self.txt), fill=self.color, tags="rec")
        self.canvas.tag_lower(self.b, self.txt)

    def gray(self):
        self.canvas.delete("all")
        self.color = "gray"
        self.txt = self.canvas.create_text(self.x, 25, text="Welcome", tags="txt")
        self.b = self.canvas.create_rectangle(self.canvas.bbox(self.txt), fill=self.color, tags="rec")
        self.canvas.tag_lower(self.b, self.txt)

    def left(self):
        if self.x < 220:
            self.canvas.delete("all")
            self.x += 2
            self.txt = self.canvas.create_text(self.x, 25, text="Welcome", tags="txt")
            self.b = self.canvas.create_rectangle(self.canvas.bbox(self.txt), fill=self.color, tags="rec")
            self.canvas.tag_lower(self.b, self.txt)

    def right(self):
        if self.x > 35:
            self.canvas.delete("all")
            self.x -= 2
            self.txt = self.canvas.create_text(self.x, 25, text="Welcome", tags="txt")
            self.b = self.canvas.create_rectangle(self.canvas.bbox(self.txt), fill=self.color, tags="rec")
            self.canvas.tag_lower(self.b, self.txt)


MainGUI()
