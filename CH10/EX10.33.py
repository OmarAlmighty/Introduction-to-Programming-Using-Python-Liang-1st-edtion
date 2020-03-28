# 10.33 (Tkinter: draw histograms) Write a program that generates 1,000 lowercase letters
# randomly, counts the occurrence of each letter, and displays a histogram for
# the occurrences, as shown in Figure 10.16a.
import random
from tkinter import *


class MainGUI:
    def __init__(self):
        window = Tk()
        self.cnvs = Canvas(window, width=550)
        self.cnvs.pack()
        self.btn = Button(window, text="Display histogram",command=self.dispHist)
        self.btn.pack()
        window.mainloop()

    def dispHist(self):
        self.cnvs.delete('all')
        counts = [0] * 26
        for i in range(1000):
            c = random.randint(0, 25)
            counts[c] += 1
        self.cnvs.create_line(0, 300, 550, 300)
        x = 0
        for i in range(26):
            c = chr(i + ord('a'))
            self.cnvs.create_text(x + 20, 305, text=c)
            x += 20
            height = counts[i]*200/max(counts)
            self.cnvs.create_rectangle(x - 10, 300, x + 10, height)

MainGUI()