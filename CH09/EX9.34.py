# 9.34 (Address book) Write a program that creates a user interface for displaying an
# address, as shown in Figure 9.40c.

from tkinter import *  # Import tkinter


class AddressBook:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("AddressBook")  # Set title

        self.nameVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Name").grid(row=1,
                                        column=1, sticky=W)
        Entry(frame1, textvariable=self.nameVar,
              width=40).grid(row=1, column=2)

        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text="Street").grid(row=1,
                                          column=1, sticky=W)
        Entry(frame2, textvariable=self.streetVar,
              width=40).grid(row=1, column=2)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="City", width=5).grid(row=1,
                                                 column=1, sticky=W)
        Entry(frame3,
              textvariable=self.cityVar).grid(row=1, column=2)
        Label(frame3, text="State").grid(row=1,
                                         column=3, sticky=W)
        Entry(frame3, textvariable=self.stateVar,
              width=5).grid(row=1, column=4)
        Label(frame3, text="ZIP").grid(row=1,
                                       column=5, sticky=W)
        Entry(frame3, textvariable=self.zipVar,
              width=5).grid(row=1, column=6)

        frame4 = Frame(window)
        frame4.pack()
        Button(frame4, text="Add",
               command=self.processAdd).grid(row=1, column=1)
        btFirst = Button(frame4, text="First",
                         command=self.processFirst).grid(row=1, column=2)
        btNext = Button(frame4, text="Next",
                        command=self.processNext).grid(row=1, column=3)
        btPrevious = Button(frame4, text="Previous", command=
        self.processPrevious).grid(row=1, column=4)
        btLast = Button(frame4, text="Last",
                        command=self.processLast).grid(row=1, column=5)

        window.mainloop()  # Create an event loop

    def processAdd(self):
        pass

    def processFirst(self):
        pass

    def processNext(self):
        pass

    def processPrevious(self):
        pass

    def processLast(self):
        pass


AddressBook()  # Create GUI

