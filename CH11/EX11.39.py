# 11.39 (Tkinter: four consecutive equal numbers) Write a GUI program for Exercise
# 11.19, as shown in Figure 11.12. Let the user enter the numbers in the text fields in
# a grid of six rows and seven columns. The user can click the Solve button to highlight
# a sequence of four equal numbers, if it exists.
import random
from tkinter import *


def isConsecutiveFour(values):
    res = []
    for i in range(len(values)):
        for j in range(len(values[i])):
            val = values[i][j]

            # search horizontally
            if j <= len(values[i]) - 4:
                v1 = values[i][j + 1]
                v2 = values[i][j + 2]
                v3 = values[i][j + 3]
                if val == v1 == v2 == v3:
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
                if val == v1 == v2 == v3:
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
                if val == v1 == v2 == v3:
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
                if val == v1 == v2 == v3:
                    res.append([i, j])
                    res.append([i + 1, j - 1])
                    res.append([i + 2, j - 2])
                    res.append([i + 3, j - 3])
                    return res
    return False


class GUI:
    def __init__(self):
        window = Tk()
        self.frame = Frame(window)
        self.frame.pack()
        self.lst = []
        for i in range(6):
            x = []
            for j in range(6):
                x.append(Text(self.frame, width=2, height=1))
                x[j].insert(INSERT, str(random.randint(0, 15)))
                x[j].grid(row=i, column=j)
            self.lst.append(x)
        btn = Button(window, text='Solve', command=self.solve)
        btn.pack()
        window.mainloop()

    def solve(self):
        values = []
        for i in range(6):
            x = []
            for j in range(6):
                x.append(int(self.lst[i][j].get("1.0", END)))
            values.append(x)
        print(values)
        res = isConsecutiveFour(values)
        print(res)
        for i in res:
            x = i[0]
            y = i[1]
            val = self.lst[x][y].get("1.0", END)
            self.lst[x][y] = Text(self.frame, width=2, height=1, bg='gray')
            self.lst[x][y].insert(INSERT, val)
            self.lst[x][y].grid(row=x, column=y)


GUI()
