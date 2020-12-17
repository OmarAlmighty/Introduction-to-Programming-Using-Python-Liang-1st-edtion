class Rectangle:
    def __init__(self,width = 1,height = 2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.height+self.width)*2