# 9.16 (Display a running fan) Write a program that displays a fan running, as shown in
# Figure 9.29a.

from tkinter import *  # Import tkinter

width = 200
height = 200
radius = 80


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("Fan")  # Set a title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        self.startingAngle = 0
        while True:
            self.startingAngle += 5
            self.displayFan(self.startingAngle)
            self.canvas.after(100)  # Sleep for 100 milliseconds
            self.canvas.update()

        window.mainloop()  # Create an event loop

    def displayFan(self, startingAngle):
        self.canvas.delete("fan")

        self.canvas.create_arc(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                               start=self.startingAngle + 0, extent=30, fill="red", tags="fan")

        self.canvas.create_arc(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                               start=self.startingAngle + 90, extent=30, fill="red", tags="fan")

        self.canvas.create_arc(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                               start=self.startingAngle + 180, extent=30, fill="red", tags="fan")

        self.canvas.create_arc(width / 2 - radius, height / 2 - radius, width / 2 + radius, height / 2 + radius,
                               start=self.startingAngle + 270, extent=30, fill="red", tags="fan")


MainGUI()
