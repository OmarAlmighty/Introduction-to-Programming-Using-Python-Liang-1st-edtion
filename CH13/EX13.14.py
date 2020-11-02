# 13.14 (Tkinter: display a graph) Rewrite Exercise 13.13 to read data from a Web URL
# such as http://cs.armstrong.edu/liang/data/graph.txt. The program should prompt the
# user to enter the URL for the file.
import urllib
from urllib import request
from tkinter import *


def readFile():
    file = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/graph.txt")
    data = []
    n = file.readline().strip()
    for i in range(int(n)):
        data.append(file.readline().strip())

    vertices = []
    for line in data:
        line = line.split()
        line = [eval(x) for x in line]
        vertices.append(line)

    return vertices


window = Tk()
cnvs = Canvas(window)
cnvs.pack()

points = readFile()

for u in points:
    x1 = u[1]
    y1 = u[2]
    v1 = points[u[3]]
    v2 = points[u[4]]
    x2 = v1[1]
    y2 = v1[2]
    x3 = v2[1]
    y3 = v2[2]
    cnvs.create_oval(x1 - 4, y1 - 4, x1 + 4, y1 + 4, fill="black")
    cnvs.create_line(x1, y1, x2, y2)
    cnvs.create_line(x1, y1, x3, y3)
    cnvs.create_text(x1 - 8, y1 - 8, text=str(u[0]))

window.mainloop()
