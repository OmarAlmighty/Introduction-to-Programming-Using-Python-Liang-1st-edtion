# 10.36 (Tkinter: linear search animation) Write a program that animates the linear
# search algorithm. Create a list that consists of 20 distinct numbers from 1 to
# 20 in a random order. The elements are displayed in a histogram, as shown in
# Figure 10.17. You need to enter a search key in the text field. Clicking the
# Step button causes the program to perform one comparison in the algorithm
# and repaints the histogram with a bar indicating the search position. When
# the algorithm is finished, display a dialog box to inform the user. Clicking the
# Reset button creates a new random list for a new start.

from tkinter import *  # Import tkinter
import tkinter.messagebox
import random


class StepControl:
    def __init__(self):
        self.list = [x for x in range(1, 20)]
        self.reset()
        self.key = 0

    def reset(self):
        self.i = -1  # current index
        self.done = False
        random.shuffle(self.list)
        self.drawAStep()

    def step(self):
        if self.done:
            tkinter.messagebox.showinfo("showinfo", "Key is found")
            return

        if self.i == -1:
            self.i += 1
        self.drawAStep()

        if self.i >= 0 and self.list[self.i] == self.key:
            self.done = True
            tkinter.messagebox.showinfo("showinfo", "Key is found")
        elif self.i >= len(self.list) - 1:
            tkinter.messagebox.showinfo("showinfo", "Key is not found")
        else:
            self.i += 1  # Continue to the next

    def drawAStep(self):
        bottomGap = 10
        canvas.delete("line")
        canvas.create_line(10, height - bottomGap, width - 10, height - bottomGap, tag="line")
        barWidth = (width - 20) / len(self.list)

        maxCount = int(max(self.list))
        for i in range(len(self.list)):
            canvas.create_rectangle(i * barWidth + 10, (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)),
                                    (i + 1) * barWidth + 10, height - bottomGap, tag="line")
            canvas.create_text(i * barWidth + 10 + barWidth / 2,
                               (height - bottomGap) * (1 - self.list[i] / (maxCount + 4)) - 8,
                               text=str(self.list[i]), tag="line")

        if self.i >= 0:
            canvas.create_rectangle(self.i * barWidth + 10,
                                    (height - bottomGap) * (1 - self.list[self.i] / (maxCount + 4)),
                                    (self.i + 1) * barWidth + 10, height - bottomGap, fill="red", tag="line")


def step():
    control.key = float(key.get())
    control.step()


def reset():
    control.reset()


window = Tk()  # Create a window
window.title("Linear Search Animation")  # Set title

width = 340
height = 150
radius = 2
canvas = Canvas(window, width=width, height=height)
canvas.pack()

frame = Frame(window)
frame.pack()

Label(frame, text="Enter a key (in float):").pack(side=LEFT)
key = StringVar()
Entry(frame, textvariable=key, justify=RIGHT, width=3).pack(side=LEFT)
Button(frame, text="Step", command=step).pack(side=LEFT)
Button(frame, text="Reset", command=reset).pack(side=LEFT)

control = StepControl()
control.drawAStep()

window.mainloop()  # Create an event loop
