# 11.38 (Turtle: draw a polygon/polyline) Write the following functions that draw a
# polygon/polyline to connect all points in the list. Each element in the list is a list of
# two coordinates.
# # Draw a polyline to connect all the points in the list
# def drawPolyline(points):
# # Draw a polygon to connect all the points in the list and
# # close the polygon by connecting the first point with the last point
# def drawPolygon(points):
# # Fill a polygon by connecting all the points in the list
# def fillPolygon(points):

import turtle


# Draw a polyline to connect all the points in the list
def drawPolyline(points):
    for i in range(len(points) - 1):
        drawLine(points[i], points[i + 1])


# Draw a polygon to connect all the points in the list and
# close the polygon by connecting the first point with the last point
def drawPolygon(points):
    drawPolyline(points)
    drawLine(points[len(points) - 1], points[0])  # Close the polygon


# Fill a polygon by connecting all the points in the list
def fillPolygon(points):
    turtle.begin_fill()
    drawPolygon(points)
    turtle.end_fill()


# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)


points = input("Enter points: ").split()

points = [eval(p) for p in points]

drawPolygon(points)