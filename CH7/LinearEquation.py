class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        denominator = self.__a * self.__d - self.__b * self.__c
        return True if denominator != 0 else False

    def getX(self):
        denominator = self.__a * self.__d - self.__b * self.__c
        numerator = self.__e * self.__d - self.__b * self.__f
        return numerator / denominator

    def getY(self):
        denominator = self.__a * self.__d - self.__b * self.__c
        numerator = self.__a * self.__f - self.__e * self.__c
        return numerator / denominator
