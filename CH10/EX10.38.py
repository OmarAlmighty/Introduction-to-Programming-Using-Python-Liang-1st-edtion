# 10.38 (Tkinter: selection-sort animation) Write a program that animates the selection-sort
# algorithm. Create a list that consists of 20 distinct numbers from 1 to 20 in a random
# order. The elements are displayed in a histogram, as shown in Figure 10.19.
# Clicking the Step button causes the program to perform an iteration of the outer
# loop in the algorithm and repaints the histogram for the new list. Color the last bar
# in the sorted sublist. When the algorithm is finished, display a dialog box to inform
# the user. Clicking the Reset button creates a new random list for a new start.

from tkinter import *  # Import tkinter
import tkinter.messagebox
import random


class StepControl:
    def __init__(self):
        self.list = [x for x in range(1, 20)]
        self.reset()
        self.key = 0

    def reset(self):
        self.i = 0  # current index
        self.done = False
        random.shuffle(self.list)
        self.drawAStep()

    def step(self):
        if self.i > len(self.list) - 1:
            tkinter.messagebox.showinfo("showinfo", "The list is already sorted")
            return

        # Find the minimum in the list[i..list.length-1]
        currentMin = self.list[self.i]
        currentMinIndex = self.i

        for j in range(self.i + 1, len(self.list)):
            if currentMin > self.list[j]:
                currentMin = self.list[j];
                currentMinIndex = j;

        # Swap list[i] with list[currentMinIndex] if necessary;
        if currentMinIndex != self.i:
            self.list[currentMinIndex] = self.list[self.i]
            self.list[self.i] = currentMin

        self.drawAStep()
        self.i += 1  # Increase step

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
    control.step()


def reset():
    control.reset()


window = Tk()  # Create a window
window.title("Selection Sort Animation")  # Set title

width = 340
height = 150
radius = 2
canvas = Canvas(window, width=width, height=height)
canvas.pack()

frame = Frame(window)
frame.pack()

Button(frame, text="Step", command=step).pack(side=LEFT)
Button(frame, text="Reset", command=reset).pack(side=LEFT)

control = StepControl()
control.drawAStep()

window.mainloop()  # Create an event loop
