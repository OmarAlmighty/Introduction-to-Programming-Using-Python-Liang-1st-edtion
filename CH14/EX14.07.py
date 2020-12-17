# 14.7 (Tkinter: Count the occurrences of each letter) Revise the preceding exercise to
# display a histogram for the result, as shown in Figure 14.6. You need to display a
# message in a message box if the URL does not exist.

import urllib.request
from tkinter import *
from tkinter import messagebox

LINE_WIDTH = 23
BASE = 550


def showResult():
    try:
        file = urllib.request.urlopen(url.get())
        lines = file.read().decode()

        counts = [0] * 26
        countLetters(lines.lower(), counts)

        cnvs.delete("data")
        cnvs.create_line(10, BASE, 595, BASE, tag="data")
        x = 12
        for i in range(26):
            cnvs.create_text(x + 2, BASE + 8, text=chr(i + ord('a')), tag="data")
            cnvs.create_rectangle(x - 9, BASE - counts[i], x + LINE_WIDTH - 9, BASE, tag="data")
            x += LINE_WIDTH
    except IOError:
        messagebox.showwarning("Analyze URL",
                               "URL " + url.get() + " does not exist")


def countLetters(lines, counts):
    for line in lines:
        for ch in line:
            if ch.isalpha():
                counts[ord(ch) - ord('a')] += 1


window = Tk()  # Create a window
window.title("Occurrence of Letters")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()

cnvs = Canvas(frame1, width=600, height=600)
cnvs.pack()

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Enter a URL: ").pack(side=LEFT)
url = StringVar()
Entry(frame2, width=20, textvariable=url).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
