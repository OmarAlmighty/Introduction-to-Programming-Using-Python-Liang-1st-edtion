# 12.11 (Tkinter: guess birthday) Listing 4.3, GuessBirthday.py, gives a program for
# guessing a birthday. Create a program for guessing birthdays as shown in Figure
# 12.23. The program prompts the user to check whether the date is in any of the
# five sets. The date is displayed in a message box upon clicking the Guess Birthday
# button.
from tkinter import *
from tkinter import messagebox


def guess():
    day = 0
    if c1var.get() == 1:
        day += 1

    if c2var.get() == 1:
        day += 2

    if c3var.get() == 1:
        day += 4

    if c4var.get() == 1:
        day += 8

    if c5var.get() == 1:
        day += 16

    messagebox.showinfo("Found it!",("Your birthday is "+str(day)))


window = Tk()
frame1 = Frame(window)
frame1.pack()
Label(frame1, text='Check the boxes if your birthday in these sets').pack()

frame2 = Frame(window)
frame2.pack()

f1 = Frame(frame2, relief='sunken')
f1.grid(row=1, column=1)
i1 = PhotoImage(file='1.GIF')
Label(f1, image=i1, relief='sunken',
      borderwidth='2p').pack()
c1var = IntVar()
Checkbutton(f1, variable=c1var, text='              ').pack()

f2 = Frame(frame2, relief='sunken')
f2.grid(row=1, column=2)
i2 = PhotoImage(file='2.GIF')
Label(f2, image=i2, relief='sunken',
      borderwidth='2p').pack()
c2var = IntVar()
Checkbutton(f2, variable=c2var, text='               ').pack()

f3 = Frame(frame2, relief='sunken')
f3.grid(row=1, column=3)
i3 = PhotoImage(file='3.GIF')
Label(f3, image=i3, relief='sunken',
      borderwidth='2p').pack()
c3var = IntVar()
Checkbutton(f3, variable=c3var, text='               ').pack()

f4 = Frame(frame2, relief='sunken')
f4.grid(row=1, column=4)
i4 = PhotoImage(file='4.GIF')
Label(f4, image=i4, relief='sunken',
      borderwidth='2p').pack()
c4var = IntVar()
Checkbutton(f4, variable=c4var, text='               ').pack()

f5 = Frame(frame2, relief='sunken')
f5.grid(row=1, column=5)
i5 = PhotoImage(file='5.GIF')
Label(f5, image=i5, relief='sunken',
      borderwidth='2p').pack()
c5var = IntVar()
Checkbutton(f5, variable=c5var, text='               ').pack()

Button(window, text='Guess Birthday', command=guess).pack()

window.mainloop()
