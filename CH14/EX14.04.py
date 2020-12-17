# 14.4 (Tkinter: Count the occurrences of each letter) Rewrite Listing 14.5 using a GUI
# program to let the user enter the file from an entry field, as shown in Figure 14.3a.
# You can also select a file by clicking the Browse button to display an Open file dialog
# box, as shown in Figure 14.3b. The file selected is then displayed in the entry
# field. Clicking the Show Result button displays the result in a text widget. You
# need to display a message in a message box if the file does not exist.

from tkinter import *  # Import tkinter
import tkinter.messagebox  # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename


def showResult():
    analyzeFile(filename.get())


def analyzeFile(filename):
    try:
        infile = open(filename, "r")  # Open the file

        counts = 26 * [0]  # Create and initialize counts
        for line in infile:
            # Invoke the countLetters function to count each letter
            countLetters(line.lower(), counts)

        # Display results
        for i in range(len(counts)):
            if counts[i] != 0:
                text.insert(END, chr(ord('a') + i) + " appears  " + str(counts[i])
                            + (" time" if counts[i] == 1 else " times") + "\n")

        infile.close()  # Close file
    except IOError:
        tkinter.messagebox.showwarning("Analyze File",
                                       "File " + filename + " does not exist")
    # Count each letter in the string


def countLetters(line, counts):
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

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=10, wrap=WORD,
            yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=openFile).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
