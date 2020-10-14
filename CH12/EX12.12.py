# 12.12 (Tkinter: a group of clocks) Write a program that displays four clocks, as shown in
# Figure 12.24.
import math
from datetime import datetime
from tkinter import *


class StillClock(Canvas):
    def __init__(self, container):
        super().__init__(container)
        self.setCurrentTime()

    def getHour(self):
        return self.__hour

    def setHour(self, hour):
        self.__hour = hour
        self.delete("clock")
        self.drawClock()

    def getMinute(self):
        return self.__minute

    def setMinute(self, minute):
        self.__minute = minute
        self.delete("clock")
        self.drawClock()

    def getSecond(self):
        return self.__second

    def setSecond(self, second):
        self.__second = second
        self.delete("clock")
        self.drawClock()

    def setCurrentTime(self):
        d = datetime.now()
        self.__hour = d.hour
        self.__minute = d.minute
        self.__second = d.second
        self.delete("clock")
        self.drawClock()

    def drawClock(self):
        width = float(self["width"])
        height = float(self["height"])
        radius = min(width, height) / 2.4
        secondHandLength = radius * 0.8
        minuteHandLength = radius * 0.65
        hourHandLength = radius * 0.5

        self.create_oval(width / 2 - radius, height / 2 - radius,
                         width / 2 + radius, height / 2 + radius, tags="clock")
        self.create_text(width / 2 - radius + 5, height / 2,
                         text="9", tags="clock")
        self.create_text(width / 2 + radius - 5, height / 2,
                         text="3", tags="clock")
        self.create_text(width / 2, height / 2 - radius + 5,
                         text="12", tags="clock")
        self.create_text(width / 2, height / 2 + radius - 5,
                         text="6", tags="clock")

        xCenter = width / 2
        yCenter = height / 2
        second = self.__second
        xSecond = xCenter + secondHandLength \
                  * math.sin(second * (2 * math.pi / 60))
        ySecond = yCenter - secondHandLength \
                  * math.cos(second * (2 * math.pi / 60))
        self.create_line(xCenter, yCenter, xSecond, ySecond,
                         fill="red", tags="clock")

        minute = self.__minute
        xMinute = xCenter + \
                  minuteHandLength * math.sin(minute * (2 * math.pi / 60))
        yMinute = yCenter - \
                  minuteHandLength * math.cos(minute * (2 * math.pi / 60))
        self.create_line(xCenter, yCenter, xMinute, yMinute,
                         fill="blue", tags="clock")

        hour = self.__hour % 12
        xHour = xCenter + hourHandLength * \
                math.sin((hour + minute / 60) * (2 * math.pi / 12))
        yHour = yCenter - hourHandLength * \
                math.cos((hour + minute / 60) * (2 * math.pi / 12))
        self.create_line(xCenter, yCenter, xHour, yHour,
                         fill="green", tags="clock")

        timestr = str(hour) + ":" + str(minute) + ":" + str(second)
        self.create_text(width / 2, height / 2 + radius + 10,
                         text=timestr, tags="clock")


window = Tk()  # Create a window
window.title("Display Clocks")  # Set title

clock1 = StillClock(window)
clock1.grid(row=1, column=1)

clock2 = StillClock(window)
clock2.grid(row=1, column=2)

clock3 = StillClock(window)
clock3.grid(row=1, column=3)

clock4 = StillClock(window)
clock4.grid(row=1, column=4)

window.mainloop()  # Create an event loop
