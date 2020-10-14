# 12.19 (Tkinter: the PieChart class) Develop a class named PieChart that extends
# Canvas for displaying a pie chart using the following constructor:
# PieChart(parent, data, width = 400, height = 300)
# Where data is a list, each element in the list is a nested list that consists of a
# value, a title for the value, and a color for the wedge in the pie chart. For example,
# for data = [[40, "CS", "red"], [30, "IS", "blue"], [50,
# "IT", "yellow"]], the pie chart is as shown in the left part of Figure 12.29.
# For data = [[140, "Freshman", "red"], [130, "Sophomore",
# "blue"], [150, "Junior", "yellow"], [80, "Senior",
# "green"]], the pie chart is as shown in the right part of Figure 12.29. Write a
# test program that displays two pie charts, as shown in Figure 12.29.
from tkinter import *


class PieChart(Canvas):
    def __init__(self, parent, data, width=400, height=300):
        super().__init__(master=parent, width=width, height=height)
        self.data = data
        self.setData(data)

    def setData(self, data):
        self.__data = data
        self.drawPieChart()

    def drawPieChart(self):
        st = 0
        sum = 0
        for d in self.__data:
            sum += d[0]

        for d in self.__data:
            size = d[0]
            lbl = d[1]
            clr = d[2]
            area = 360 / sum * size
            self.create_arc(70, 70, 260, 260, start=st, extent=area, fill=clr)
            # self.create_text(st, st , text=lbl) #Does not work properly with me :)
            if st > area:
                st = st + area
            else:
                st = area



class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("PieChart Reusable Class")  # Set title

        canvas1 = PieChart(window, [[40, 'CS', 'red'], [30, "IS", "blue"], [50, "IT", "yellow"]])
        canvas1.grid(row=1, column=1)
        canvas1.drawPieChart()

        canvas2 = PieChart(window, [[140, "Freshman", "red"], [130, "Sophomore", "blue"],
                                    [150, "Junior", "yellow"], [80, "Senior", "green"]])
        canvas2.grid(row=1, column=2)
        canvas2.drawPieChart()

        window.mainloop()  # Create an event loop


MainGUI()
