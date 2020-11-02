# 13.13 (Tkinter: display a graph) A graph consists of vertices and edges that connect
# vertices. Write a program that reads a graph from a file and displays it on a
# panel. The first line in the file contains a number that indicates the number of
# vertices (n). The vertices are labeled as 0, 1, ..., n-1. Each subsequent line, with
# the format u x y v1, v2, ..., describes that the vertex u is located at position
# (x, y) with the edges (u, v1), (u, v2), and so on. Figure 13.12a gives an example
# of the file for a graph. Your program prompts the user to enter the name of the
# file, reads data from the file, and displays the graph on a panel, as shown in
# Figure 13.12b.
from tkinter import *


def readFile():
    file = open("graph.txt", "r")
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
