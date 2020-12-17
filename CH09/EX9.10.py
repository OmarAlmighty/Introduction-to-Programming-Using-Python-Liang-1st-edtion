# 9.10 (Display a pie chart) Write a program that uses a pie chart to display the percentages
# of the overall grade represented by the project, quizzes, the midterm exam,
# and the final exam, as shown in Figure 9.26b. Suppose that project is weighted as
# 20 percent of the grade and is displayed in red, quizzes are 10 percent and are displayed
# in blue, the midterm exam is 30 percent and is displayed in green, and the
# final exam is 40 percent and is displayed in orange.
from tkinter import *  # Import tkinter
import math

radius = 100
width = 300
height = 300


class MainGUI:
    def drawAPie(self, start, extent, color, title):
        self.canvas.create_arc(width / 2 - radius, height / 2 - radius,
                               width / 2 + radius, height / 2 + radius,
                               start=start, extent=extent, fill=color)
        x = width / 2 + radius * math.cos(math.radians(extent / 2 + start))
        y = height / 2 - radius * math.sin(math.radians(extent / 2 + start))
        self.canvas.create_text(x, y, text=title)

    def __init__(self):
        window = Tk()  # Create a window
        window.title("Pie Chart")  # Set a title

        self.canvas = Canvas(window, bg="white", width=width, height=height)
        self.canvas.pack()

        self.drawAPie(0, 360 * 0.2, "red", "Project -- 20%")
        self.drawAPie(360 * 0.2, 360 * 0.1, "blue", "Quizzes -- 10%")
        self.drawAPie(360 * 0.2 + 360 * 0.1, 360 * 0.3, "green", "Midterm -- 30%")
        self.drawAPie(360 * 0.2 + 360 * 0.1 + 360 * 0.3, 360 * 0.4, "orange", "Final -- 40%")

        window.mainloop()  # Create an event loop


MainGUI()