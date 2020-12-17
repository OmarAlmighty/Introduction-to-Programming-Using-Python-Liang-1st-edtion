# 9.11 (Display a clock) Write a program that displays a clock to show the current time,
# as shown in Figure 9.27a. To obtain the current time, use the datetime class in
# Supplement II.B.
from datetime import datetime
from tkinter import *

now = datetime.now().strftime("%H:%M:%S")

window = Tk()
c = Canvas(window, width=500, height=500, bg="white")
c.pack()
c.create_oval(50, 50, 450, 450)
c.create_text(250, 50, text="12")
c.create_text(50, 250, text="9")
c.create_text(450, 250, text="3")
c.create_text(250, 450, text="6")
c.create_text(250, 470, text=now)
c.create_line(250,250,100,160,width=2)
c.create_line(250,250,230,360,width="3")
c.create_line(250,250,300,300)


window.mainloop()
