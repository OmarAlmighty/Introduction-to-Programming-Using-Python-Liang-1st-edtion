# 12.18 (Tkinter: the BarChart class) Develop a class named BarChart that extends
# Canvas for displaying a bar chart:
# BarChart(parent, data, width = 400, height = 300)
# Where data is a list, each element in the list is a nested list that consists of a
# value, a title for the value, and a color for the bar in the bar chart. For example,
# for data = [[40, "CS", "red"], [30, "IS", "blue"], [50, "IT",
# "yellow"]], the bar chart is as shown in the left part of Figure 12.28. For data
# = [[140, "Freshman", "red"], [130, "Sophomore", "blue"],
# [150, "Junior", "yellow"], [80, "Senior", "green"]], the bar
# chart is as shown in the right part of Figure 12.28. Write a test program that displays
# two bar charts, as shown in Figure 12.28.

from tkinter import *  # Import tkinter

width = 300
height = 200


class BarChart(Canvas):
    def __init__(self, parent, data, width=400, height=300):
        super().__init__(parent, width=width, height=height)
        self.setData(data)

    def setData(self, data):
        self.__data = data
        self.drawBarChart()

    def drawBarChart(self):
        bottomGap = 15
        self.create_line(10, height - bottomGap, width - 10, height - bottomGap)
        barWidth = (width - 20) / len(self.__data)

        values = []
        for x, y, z in self.__data:
            values.append(x)

        maxCount = int(max(values))
        for i in range(len(self.__data)):
            self.create_rectangle(i * barWidth + 10, height - (height - 10) * self.__data[i][0] / maxCount,
                                  (i + 1) * barWidth + 10, height - bottomGap, fill=self.__data[i][2])

            self.create_text(i * barWidth + 10 + barWidth / 2, height - bottomGap / 2,
                             text=self.__data[i][1])


class MainGUI:
    def __init__(self):
        window = Tk()  # Create a window
        window.title("BarChart Reusable Class")  # Set title

        canvas1 = BarChart(window, [[40, "CS", "red"], [30, "IS", "blue"], [50, "IT", "yellow"]], width=width,
                           height=height)
        canvas1.grid(row=1, column=1)
        canvas2 = BarChart(window,
                           [[140, "Freshman", "red"], [130, "Sophomore", "blue"], [150, "Junior", "yellow"],
                            [80, "Senior", "green"]],
                           width=width, height=height)
        canvas2.grid(row=1, column=2)

        window.mainloop()  # Create an event loop


MainGUI()
