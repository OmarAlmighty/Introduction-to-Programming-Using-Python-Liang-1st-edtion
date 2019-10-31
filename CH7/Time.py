import time


class Time:
    def __init__(self):
        self.setTime(int(time.time()))

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, elapsedTime):
        self.__second = elapsedTime % 60

        totalMinutes = elapsedTime // 60

        self.__minute = totalMinutes % 60

        totalHours = totalMinutes // 60

        self.__hour = totalHours % 24
