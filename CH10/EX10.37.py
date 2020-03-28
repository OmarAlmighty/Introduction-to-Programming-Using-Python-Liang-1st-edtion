# 10.37 (Tkinter: binary search animation) Write a program that animates the binary
# search algorithm. Create a list with the numbers from 1 to 20 in this order. The
# elements are displayed in a histogram, as shown in Figure 10.18. You need to
# enter a search key in the text field. Clicking the Step button causes the program
# to perform one comparison in the algorithm. Use a light-gray color to paint the
# bars for the numbers in the current search range and use a red color to paint the
# bar indicating the middle number in the search range. When the algorithm is
# finished, display a dialog box to inform the user. Clicking the Reset button
# enables a new search to start. This button also makes the text field editable.
import tkinter.messagebox
from tkinter import *


class MainGUI:
    def __init__(self):
        self.lst = [x for x in range(1, 21)]
        width = 380
        height = 150
        window = Tk()
        self.cnvs = Canvas(window, width=width, height=height)
        self.cnvs.pack()
        frame = Frame(window)
        frame.pack()
        Label(frame, text="Enter a key (in float):").pack(side=LEFT)
        self.key = StringVar()
        Entry(frame, textvariable=self.key, justify=RIGHT, width=3).pack(side=LEFT)
        Button(frame, text="Step", command=self.step).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)
        self.reset()
        window.mainloop()

    def reset(self):
        self.found = False
        self.click = 1  # for counting number of click an odd click colors a bar with red and an even number of
        # clicks colors the bars to white
        self.r = len(self.lst) - 1
        self.l = 0
        x = 5
        y = 140
        self.recs = []
        for i in range(20):
            rect = self.cnvs.create_rectangle(x, 140, x + 18, y - 7, fill='lightgray')
            self.recs.append(rect)
            self.cnvs.create_text(x + 10, y-18, text=str(i + 1))
            x += 18
            y -= 6

    def step(self):
        k = int(self.key.get())
        if not self.found:
            mid = (self.l + self.r) // 2
            self.cnvs.itemconfig(self.recs[mid], fill='red')  # mark current with red
            if self.click % 2 == 0:
                if mid + 1 == k:
                    tkinter.messagebox.showinfo("showinfo", "Key is found")
                    self.found = True
                else:
                    if k > self.lst[mid]:
                        self.l = mid + 1
                        for i in range(self.l):
                            self.cnvs.itemconfig(self.recs[i], fill='white')  # change to white
                    else:
                        self.r = mid - 1
                        for i in range(self.r + 1, len(self.lst)):
                            self.cnvs.itemconfig(self.recs[i], fill='white')

            if not self.found and self.l > self.r:
                tkinter.messagebox.showinfo("showinfo", "Key is not found")  # change to white
        self.click += 1


MainGUI()
