# 14.5 (Tkinter: Count the occurrences of each letter) Revise the preceding exercise to
# display a histogram for the result, as shown in Figure 14.4. You need to display a
# message in a message box if the file does not exist.

from tkinter import *  # Import tkinter
import tkinter.messagebox  # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename

LINE_WIDTH = 23
BASE = 350

def showResult():
    file = open(filename.get(), 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].lower()
    counts = [0] * 26
    countLetters(lines, counts)

    cnvs.delete("data")
    cnvs.create_line(10, BASE, 595, BASE, tag="data")
    x = 12
    for i in range(26):
        cnvs.create_text(x+2, BASE+8, text=chr(i + ord('a')),tag="data")
        cnvs.create_rectangle(x-9, BASE-counts[i], x + LINE_WIDTH-9, BASE,tag="data")
        x += LINE_WIDTH


def countLetters(lines, counts):
    for line in lines:
        for ch in line:
            if ch.isalpha():
                counts[ord(ch) - ord('a')] += 1


def openFile():
    filenameforReading = askopenfilename()
    filename.set(filenameforReading)


window = Tk()  # Create a window
window.title("Occurrence of Letters")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()

cnvs = Canvas(frame1, width=600,height=400)
cnvs.pack()

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=openFile).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
