# 9.7 (Display an grid ) Write a program that displays an grid, as shown in
# Figure 9.25c. Use red for vertical lines and blue for horizontal lines.
from tkinter import *

window = Tk()
c = Canvas(window,bg="white",width=570,height=570)
c.pack()
for i in range(11):
    c.create_line(10+(i*70),10,10+(i*70),570,fill="red")

for i in range(11):
    c.create_line(10,10+(i*70),570,10+(i*70),fill="blue")

window.mainloop()