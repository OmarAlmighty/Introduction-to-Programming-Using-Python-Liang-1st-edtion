# 9.3 (Select geometric figures) Write a program that draws a rectangle or an oval, as
# shown in Figure 9.23. The user selects a figure from a radio button and specifies
# whether it is filled by selecting a check button.

from tkinter import *


class GUI:
    def __init__(self):
        window = Tk()
        self.v1 = IntVar()
        self.v2 = IntVar()
        self.c = Canvas(window, width=200, height=200, bg="white")
        self.c.pack()
        f = Frame(window)
        rrb = Radiobutton(f, text="Rectangle", variable=self.v1, value=1, command=self.draw).grid(row=1, column=1)
        orb = Radiobutton(f, text="Oval", variable=self.v1, value=2, command=self.draw).grid(row=1, column=2)
        fillcb = Checkbutton(f, text="Filled", variable=self.v2).grid(row=1, column=3)
        f.pack()

        window.mainloop()

    def draw(self):
        self.c.delete("r","o")
        if self.v2.get() == 1:
            if self.v1.get() == 1:
                self.c.create_rectangle(10, 10, 200, 100, fill="blue", tag="r")
            else:
                self.c.create_oval(10, 10, 200, 100, fill="blue", tag="o")
        else:
            if self.v1.get() == 1:
                self.c.create_rectangle(10, 10, 200, 100,tag="r")
            else:
                self.c.create_oval(10, 10, 200, 100,tag="o")


GUI()
