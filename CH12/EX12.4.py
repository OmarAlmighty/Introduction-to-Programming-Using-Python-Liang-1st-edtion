# 12.4 (Geometry: find the bounding rectangle) A bounding rectangle is the minimum
# rectangle that encloses a set of points in a two-dimensional plane, as shown in
# Figure 12.16. Write a method that returns a bounding rectangle for a set of points
# in a two-dimensional plane, as follows:
# def getRectangle(points):
# You defined the Rectangle2D class in Exercise 8.19. Write a test program that
# prompts the user to enter the points as x1 y1 x2 y2 x3 y3 ... in one line, and displays
# the bounding rectangle’s center, width, and height.
import math


class Rectangle2D:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.__x__ = x
        self.__y__ = y
        self.__w__ = width
        self.__h__ = height

    def getX(self):
        return self.__x__

    def getY(self):
        return self.__y__

    def getWidth(self):
        return self.__w__

    def getHeight(self):
        return self.__h__

    def setX(self, x):
        self.__x__ = x

    def setY(self, y):
        self.__y__ = y

    def setWidth(self, width):
        self.__w__ = width

    def setHeight(self, height):
        self.__h__ = height

    def getArea(self):
        return self.__w__ * self.__h__

    def getPerimeter(self):
        return (self.__w__ + self.__h__) * 2

    def containsPoint(self, x, y):
        return abs(x - self.__x__) <= self.__w__ / 2 and abs(y - self.__y__) <= self.__h__ / 2

    def contains(self, rect):
        dis = math.sqrt((self.__x__ - rect.getX()) ** 2 + (self.__y__ - rect.getY()) ** 2)
        return True if dis + rect.getWidth() <= self.__w__ and dis + rect.getHeight() <= self.__h__ else False

    def overlaps(self, rect):
        return not (self.__x__ <= rect.__x__ or self.__x__ <= self.__w__
                    or ((rect.__x__ + rect.__w__) <= (self.__x__ + self.__w__))
                    or ((rect.__y__ + rect.__h__) <= (self.__y__ + self.__h__)))

    def __contains__(self, rect):
        return True if rect.contains(self) else False

    def __lt__(self, rect):
        return self.__cmp__(rect) < 0

    def __le__(self, rect):
        return self.__cmp__(rect) <= 0

    def __eq__(self, rect):
        return self.__cmp__(rect) == 0

    def __ne__(self, rect):
        return self.__cmp__(rect) != 0

    def __gt__(self, rect):
        return self.__cmp__(rect) > 0

    def __ge__(self, rect):
        return self.__cmp__(rect) >= 0


def getRectangle(points):
    minX = maxX = minY = maxY = points[0][0]

    for i in range(len(points)):
        if minX > points[i][0]:
            minX = points[i][0]

        if minY > points[i][1]:
            minY = points[i][1]

    for i in range(len(points)):
        if maxX < points[i][0]:
            maxX = points[i][0]

        if maxY < points[i][1]:
            maxY = points[i][1]

    return Rectangle2D((minX + maxX) / 2, (minY + maxY) / 2, maxX - minX, maxY - minY)


def main():
    points = input("Enter the points: ").strip().split()
    points = [[eval(points[i]), eval(points[i + 1])] for i in range(0, len(points) - 1, 2)]

    rect = getRectangle(points)
    print("The bounding rectangle is centered at (" + str(rect.getX()) + ", " + str(rect.getY()) + \
          ") with width " + str(rect.getWidth()) + " and height " + str(rect.getHeight()))


main()