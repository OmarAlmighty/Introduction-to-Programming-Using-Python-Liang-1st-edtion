# 11.47 (Tkinter: largest block) Write a program that displays a 10 *10 square matrix, as
# shown in Figure 11.17b. Each element in the matrix is a 0 or 1, randomly generated
# with a click of the Refresh button. Display each number centered in a text box.
# Allow the user to change the entry value. Click the Find Largest Block button to find
# a largest square submatrix that consists of 1s. Highlight the numbers in the block, as
# shown in Figure 11.17c.
import random
from tkinter import *


class GUI:
    def __init__(self):
        window = Tk()
        self.frame = Frame(window)
        self.frame.pack()
        self.lst = []
        for i in range(10):
            x = []
            for j in range(10):
                x.append(Text(self.frame, width=2, height=1))
                x[j].tag_configure("center", justify='center')
                x[j].insert('1.0', str(random.randint(0, 1)))
                x[j].tag_add("center", "1.0", "end")
                x[j].grid(row=i, column=j)
            self.lst.append(x)
        btn = Button(window, text='Refresh', command=self.refresh)
        btn2 = Button(window, text='Find largest block', command=self.find)
        btn2.pack()
        btn.pack()

        window.mainloop()

    def refresh(self):
        for i in range(len(self.lst)):
            for j in range(len(self.lst[1])):
                self.lst[i][j].delete('1.0', END)
                self.lst[i][j].tag_configure("center", justify='center')
                self.lst[i][j].insert('1.0', str(random.randint(0, 1)))
                self.lst[i][j].tag_add("center", "1.0", "end")

    def find(self):
        values = []
        for i in range(10):
            x = []
            for j in range(10):
                x.append(int(self.lst[i][j].get("1.0", END)))
            values.append(x)

        # Construct a sum matrix S[R][C] for the given M[R][C].
        w = len(values)
        h = len(values[1])
        sum = [[0 for x in range(w)] for y in range(h)]

        # Copy first row and first columns as it is from M[][] to S[][]
        sum[0] = values[0]
        for i in range(len(values)):
            sum[i][0] = values[i][0]

        # For other entries, use following expressions to construct S[][]
        for i in range(1, w):
            for j in range(1, h):
                if values[i][j] == 1:
                    sum[i][j] = min(sum[i][j - 1], sum[i - 1][j],
                                    sum[i - 1][j - 1]) + 1

        # Find the maximum entry in S[R][C]
        maxIndx = []
        max = -1
        for i in range(len(values)):
            for j in range(len(values[0])):
                if sum[i][j] > max:
                    maxIndx = []
                    maxIndx.append(i)
                    maxIndx.append(j)
                    max = sum[i][j]
                elif sum[i][j] == max:
                    maxIndx.append(i)
                    maxIndx.append(j)

        # select an entry
        x = maxIndx[0]
        y = maxIndx[1]
        for i in range(x, x - max, -1):
            for j in range(y, y - max, -1):
                val = self.lst[i][j].get("1.0", END)
                self.lst[i][j] = Text(self.frame, width=2, height=1, bg='gray')
                self.lst[i][j].tag_configure("center", justify='center')
                self.lst[i][j].insert(INSERT, val)
                self.lst[i][j].tag_add("center", "1.0", "end")
                self.lst[i][j].grid(row=i, column=j)

        sum = [[str(x) for x in l] for l in sum]
        print('\n'.join(map(', '.join, sum)))
        print(maxIndx)

GUI()
