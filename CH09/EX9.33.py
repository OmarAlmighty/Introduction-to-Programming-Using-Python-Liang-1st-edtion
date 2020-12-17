# 9.33 (Draw an arrow line) Write a program that randomly draws an arrow line when
# the Draw a Random Arrow Line button is clicked, as shown in Figure 9.40b.
import random
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, width=300, height=300, bg="white")
        self.canvas.pack()
        btn = Button(window, text="Draw a random arrow line", command=self.draw)
        btn.pack()

        window.mainloop()

    def draw(self):
        self.canvas.delete("line")
        x1 = random.randint(5, 290)
        y1 = random.randint(5, 290)
        x2 = random.randint(5, 290)
        y2 = random.randint(5, 290)
        self.canvas.create_line(x1, y1, x2, y2, arrow=LAST, tags="line")


MainGUI()
