# 8.19 (Geometry: The Rectangle2D class) Define the Rectangle2D class that
# contains:
# ■ Two float data fields named x and y that specify the center of the rectangle
# with get/set methods. (Assume that the rectangle sides are parallel to x- or yaxes.)
# ■ The data fields width and height with get/set methods.
# ■ A constructor that creates a rectangle with the specified x, y, width, and
# height with default values 0.
# ■ A method getArea() that returns the area of the rectangle.
# ■ A method getPerimeter() that returns the perimeter of the rectangle.
# ■ A method containsPoint(x, y) that returns True if the specified point (x,
# y) is inside this rectangle (see Figure 8.11a).
# ■ A method contains(Rectangle2D) that returns True if the specified
# rectangle is inside this rectangle (see Figure 8.11b).
# ■ A method overlaps(Rectangle2D) that returns True if the specified
# rectangle overlaps with this rectangle (see Figure 8.11c).
# ■ Implement the __contains__(another) method that returns True if this
# rectangle is contained in another rectangle.
# ■ Implement the _ _cmp__, __lt__, __le_ _, __eq_ _, __ne__, __gt__,
# __ge__ methods that compare two circles based on their areas.
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


def main():
    x1, y1, w1, h1 = eval(input("Enter x1, y1, width1, height1: "))
    x2, y2, w2, h2 = eval(input("Enter x2, y2, width2, height2: "))
    r1 = Rectangle2D(x1, y1, w1, h1)
    r2 = Rectangle2D(x2, y2, w2, h2)
    print("Area for r1 is", r1.getArea())
    print("Perimeter for r1", r1.getPerimeter())
    print("Area for r2 is", r2.getArea())
    print("Perimeter for r2", r2.getPerimeter())
    print("r1 contains the center of r2?", r1.containsPoint(r2.getX(), r2.getY()))
    print("r1 contains r2?", r1.contains(r2))
    print("r1 overlaps r2?", r1.overlaps(r2))


main()
