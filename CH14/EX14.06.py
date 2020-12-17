# 14.6 (Tkinter: Count the occurrences of each letter) Rewrite Listing 14.5 using a GUI
# program to let the user enter the URL from an entry field, as shown in Figure 14.5.
# Clicking the Show Result button displays the result in a text widget. You need to
# display a message in a message box if the URL does not exist.
import urllib.request
from tkinter import *
from tkinter import messagebox


def showResult():

    try:
        filename = urllib.request.urlopen(url.get())
        infile = filename.read().decode()
        counts = 26 * [0]  # Create and initialize counts
        for line in infile:
            # Invoke the countLetters function to count each letter
            countLetters(line.lower(), counts)

        # Display results
        for i in range(len(counts)):
            if counts[i] != 0:
                text.insert(END, chr(ord('a') + i) + " appears  " + str(counts[i])
                            + (" time" if counts[i] == 1 else " times") + "\n")

    except IOError:
        messagebox.showwarning("Analyze URL",
                               "URL " + url.get() + " does not exist")
    # Count each letter in the string


def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1


window = Tk()  # Create a window

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

Label(frame2, text="Enter a URL: ").pack(side=LEFT)
url = StringVar()
Entry(frame2, width=30, textvariable=url).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
