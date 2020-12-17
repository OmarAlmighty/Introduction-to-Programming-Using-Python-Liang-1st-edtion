import time


class StopWatch:
    def __init__(self):
        self.__startTime = time.time()

    def getStartTime(self):
        return self.__startTime

    def start(self):
        self.__startTime = time.time()

    def end(self):
        self.__endTime = time.time()

    def getElapsedTime(self):
        return int(1000 * (self.__endTime - self.__startTime))
