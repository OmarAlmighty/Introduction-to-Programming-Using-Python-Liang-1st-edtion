# 9.9 (Display a bar chart) Write a program that uses a bar chart to display the percentages
# of the overall grade represented by the project, quizzes, the midterm exam,
# and the final exam, as shown in Figure 9.26a. Suppose that the project is 20 percent
# of the grade and its value is displayed in red, quizzes are 10 percent and are
# displayed in blue, the midterm exam is 30 percent and is displayed in green, and
# the final exam is 40 percent and is displayed in orange.
from tkinter import *

window = Tk()
c = Canvas(window, width=500, height=200, bg="white")
c.pack()

c.create_line(2, 190, 500, 190)

c.create_rectangle(10, 190, 100, 100, fill="red")
c.create_text(50, 90, text="project --20%")

c.create_rectangle(110, 190, 200, 140, fill="blue")
c.create_text(160, 130, text="quizzes --10%")

c.create_rectangle(210, 190, 300, 120, fill="green")
c.create_text(260, 110, text="midterm --30%")

c.create_rectangle(310, 190, 400, 95, fill="orange")
c.create_text(350, 80, text="final --40%")

window.mainloop()
