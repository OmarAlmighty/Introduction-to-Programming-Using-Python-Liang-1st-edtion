# 9.8 (Display numbers in a triangular pattern) Write a program that displays numbers
# in a triangular pattern, as shown in Figure 9.25d. The number of lines in the display
# changes to fit the window as the window resizes.
from tkinter import *

window = Tk()
width = 300
height = 300
canvas = Canvas(window, bg="white", width=width, height=height)
canvas.pack()

for i in range(1, 12):
    s = ""
    for j in range(1, i + 1):
        s += str(j) + " "
    canvas.create_text(width / 2, i * height / 12, text=s, fill="red")
window.mainloop()  # Create an event loop
