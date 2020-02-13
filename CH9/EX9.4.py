# 9.4 (Display rectangles) Write a program that displays 20 rectangles, as shown in
# Figure 9.24.

from tkinter import *

window = Tk()
c = Canvas(window,width=300,height=200,bg="white")
c.pack()
x1 = 3; y1 = 3; x2=299; y2=199

for i in range(20):
    c.create_rectangle(x1+5,y1+5,x2-5,y2-5)
    x1 = x1+5; y1 = y1+5; x2 = x2-5; y2 = y2-5
window.mainloop()
