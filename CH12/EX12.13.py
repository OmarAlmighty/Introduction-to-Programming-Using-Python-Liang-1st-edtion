# 12.13 (Tkinter: Connect Four game) In Eself.xercise 11.20, self.you created a Connect Four
# game that enables two plaself.yers to plaself.y the game on the console. Rewrite the program
# using a GUI program, as shown in Figure 12.25. The program enables
# two plaself.yers to place self.red and self.self.yellow disks in self.turn. To place a disk, the plaself.yer
# needs to click on an available cell. An available cell is unoccupied and its
# downward neighbor is occupied. The program flashes the four winning cells if
# a plaself.yer wins, and reports no winners if all cells are occupied with no winners.
from tkinter import *
import time


class GUI:
    def __init__(self):
        window = Tk()
        frame1 = Frame(window)
        frame1.pack()
        self.buttons = []
        self.values = []
        self.img = PhotoImage(file='cell.GIF')
        self.red = PhotoImage(file="red.GIF")
        self.yellow = PhotoImage(file="yellow.GIF")
        self.turn = 0  # 0 for red, 1 for self.yellow
        self.x = 0
        self.y = 0
        for i in range(7):
            self.buttons.append([])
            self.values.append([])
            for j in range(7):
                self.values[i].append(-1)
                b = Button(frame1, image=self.img, command=lambda id=(str(self.x) + ' ' + str(self.y)): self.check(id))
                b.grid(row=i + 1, column=j + 1)
                self.buttons[i].append(b)
                self.y += 1
            self.x += 1
            self.y = 0

        self.btn = Button(window, text="Start over", command=self.replay)
        self.btn.pack()
        window.mainloop()

    def check(self, id):
        x, y = id.split()
        x = int(x)
        y = int(y)

        if self.turn == 0:
            self.buttons[x][y].configure(image=self.red)
            self.values[x][y] = 0
            self.turn = 1
        else:
            self.buttons[x][y].configure(image=self.yellow)
            self.values[x][y] = 1
            self.turn = 0

        res = self.isConsecutiveFour(self.values)
        if res:
            self.buttons[res[0][0]][res[0][1]].configure(background="blue")
            self.buttons[res[1][0]][res[1][1]].configure(background="blue")
            self.buttons[res[2][0]][res[2][1]].configure(background="blue")
            self.buttons[res[3][0]][res[3][1]].configure(background="blue")

    def isConsecutiveFour(self, values):
        res = []
        for i in range(len(values)):
            for j in range(len(values[i])):
                val = values[i][j]

                # search horizontally
                if j <= len(values[i]) - 4:
                    v1 = values[i][j + 1]
                    v2 = values[i][j + 2]
                    v3 = values[i][j + 3]
                    if val == v1 == v2 == v3 == 0 or val == v1 == v2 == v3 == 1:
                        res.append([i, j])
                        res.append([i, j + 1])
                        res.append([i, j + 2])
                        res.append([i, j + 3])
                        return res

                # search vertically
                if i <= len(values) - 4:
                    v1 = values[i + 1][j]
                    v2 = values[i + 2][j]
                    v3 = values[i + 3][j]
                    if val == v1 == v2 == v3 == 0 or val == v1 == v2 == v3 == 1:
                        res.append([i, j])
                        res.append([i + 1, j])
                        res.append([i + 2, j])
                        res.append([i + 3, j])
                        return res

                # search diagonally
                if i <= len(values) - 4 and j <= len(values[i]) - 4:
                    v1 = values[i + 1][j + 1]
                    v2 = values[i + 2][j + 2]
                    v3 = values[i + 3][j + 3]
                    if val == v1 == v2 == v3 == 0 or val == v1 == v2 == v3 == 1:
                        res.append([i, j])
                        res.append([i + 1, j + 1])
                        res.append([i + 2, j + 2])
                        res.append([i + 3, j + 3])
                        return res

                # search diagonally
                if i <= len(values) - 4 and j >= 3:
                    v1 = values[i + 1][j - 1]
                    v2 = values[i + 2][j - 2]
                    v3 = values[i + 3][j - 3]
                    if val == v1 == v2 == v3 == 0 or val == v1 == v2 == v3 == 1:
                        res.append([i, j])
                        res.append([i + 1, j - 1])
                        res.append([i + 2, j - 2])
                        res.append([i + 3, j - 3])
                        return res
        return False

    def replay(self):
        self.doFlash = False
        for i in range(len(self.values)):
            for j in range(len(self.values[i])):
                self.values[i][j] = -1
                self.buttons[i][j].configure(image=self.img, bg="white")


GUI()
