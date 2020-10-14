# 12.5 (Game: Tic-tac-toe) Write a program that plays the tic-tac-toe game. Two players
# take turns clicking an available cell in a grid with their respective tokens
# (either X or O). When one player has placed three tokens in a horizontal, vertical,
# or diagonal row on the grid, the game is over and that player has won. A draw (no
# winner) occurs when all the cells in the grid have been filled with tokens and neither
# player has achieved a win. Figure 12.17 shows the representative sample runs
# of the example.Assume that all the cells are initially empty, and that the first player takes the X
# token and the second player the O token. To mark a cell, the player points the
# mouse to the cell and clicks it. If the cell is empty, the token (X or O) is displayed.
# If the cell is already filled, the player’s action is ignored.
# Define a custom class named Cell that extends Label for displaying a token and
# for responding to the button-click event. The class contains a data field token with
# three possible values—' ', X, and O—that denote whether the cell has been occupied
# and which token is used in the cell if it is occupied.
# The three image files x.gif, o.gif, and empty.gif can be obtained from
# cs.armstrong.edu/liang/py/book.zip in the image folder. Use these three images
# to display the X, O, and empty cells.

from tkinter import *


class Cell(Label):

    def __init__(self, container, row, col):
        super().__init__(container)
        img = PhotoImage(file='empty.gif')
        self["image"] = img
        self.image = img  # keep a reference!
        self.__row = row
        self.__col = col
        self.grid(row=self.__row, column=self.__col)

    def setImage(self, i):
        img = PhotoImage(file=i)
        self["image"] = img
        self.image = img  # keep a reference!


class Main():
    def __init__(self):
        window = Tk()
        self.frame = Frame(window)
        self.frame.pack()
        self.turn = 'x'
        self.board = []
        for i in range(3):
            self.board.append([])
            for j in range(3):
                self.board[i].append(-1)  # Empty

        self.cell00 = Cell(self.frame, 0, 0)
        self.cell00.bind('<Button-1>', self.setImage0)
        self.cell01 = Cell(self.frame, 0, 1)
        self.cell01.bind('<Button-1>', self.setImage1)
        self.cell02 = Cell(self.frame, 0, 2)
        self.cell02.bind('<Button-1>', self.setImage2)

        self.cell10 = Cell(self.frame, 1, 0)
        self.cell10.bind('<Button-1>', self.setImage3)
        self.cell11 = Cell(self.frame, 1, 1)
        self.cell11.bind('<Button-1>', self.setImage4)
        self.cell12 = Cell(self.frame, 1, 2)
        self.cell12.bind('<Button-1>', self.setImage5)

        self.cell20 = Cell(self.frame, 2, 0)
        self.cell20.bind('<Button-1>', self.setImage6)
        self.cell21 = Cell(self.frame, 2, 1)
        self.cell21.bind('<Button-1>', self.setImage7)
        self.cell22 = Cell(self.frame, 2, 2)
        self.cell22 = Cell(self.frame, 2, 2)
        self.cell22.bind('<Button-1>', self.setImage8)

        fram = Frame(window)
        fram.pack()
        self.lbl = Label(fram)
        self.lbl.pack()
        window.mainloop()

    def setImage0(self, event=None):
        if self.turn == 'x':
            self.cell00.setImage('x.gif')
            if self.board[0][0] == -1:
                self.board[0][0] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell00.setImage('o.gif')
            if self.board[0][0] == -1:
                self.board[0][0] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def setImage1(self, event=None):
        if self.turn == 'x':
            self.cell01.setImage('x.gif')
            if self.board[0][1] == -1:
                self.board[0][1] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell01.setImage('o.gif')
            if self.board[0][1] == -1:
                self.board[0][1] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def setImage2(self, event=None):
        if self.turn == 'x':
            self.cell02.setImage('x.gif')
            if self.board[0][2] == -1:
                self.board[0][2] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell02.setImage('o.gif')
            if self.board[0][2] == -1:
                self.board[0][2] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def setImage3(self, event=None):
        if self.turn == 'x':
            self.cell10.setImage('x.gif')
            if self.board[1][0] == -1:
                self.board[1][0] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell10.setImage('o.gif')
            if self.board[1][0] == -1:
                self.board[1][0] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def setImage4(self, event=None):
        if self.turn == 'x':
            self.cell11.setImage('x.gif')
            if self.board[1][1] == -1:
                self.board[1][1] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell11.setImage('o.gif')
            if self.board[1][1] == -1:
                self.board[1][1] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def setImage5(self, event=None):
        if self.turn == 'x':
            self.cell12.setImage('x.gif')
            if self.board[1][2] == -1:
                self.board[1][2] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell12.setImage('o.gif')
            if self.board[1][2] == -1:
                self.board[1][2] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def setImage6(self, event=None):
        if self.turn == 'x':
            self.cell20.setImage('x.gif')
            if self.board[2][0] == -1:
                self.board[2][0] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell20.setImage('o.gif')
            if self.board[2][0] == -1:
                self.board[2][0] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def setImage7(self, event=None):
        if self.turn == 'x':
            self.cell21.setImage('x.gif')
            if self.board[2][1] == -1:
                self.board[2][1] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell21.setImage('o.gif')
            if self.board[2][1] == -1:
                self.board[2][1] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def setImage8(self, event=None):
        if self.turn == 'x':
            self.cell22.setImage('x.gif')
            if self.board[2][2] == -1:
                self.board[2][2] = 1  # 1 is x
                if self.isWin(self.board, 1):
                    self.lbl['text'] = "Player X won!"
            self.turn = 'o'
        else:
            self.cell22.setImage('o.gif')
            if self.board[2][2] == -1:
                self.board[2][2] = 0  # 0 is o
                if self.isWin(self.board, 0):
                    self.lbl['text'] = "Player O won!"
            self.turn = 'x'

    def isWin(self, board, c):
        if board[0][0] == board[0][1] == board[0][2] == c or \
                board[1][0] == board[1][1] == board[1][2] == c or \
                board[2][0] == board[2][1] == board[2][2] == c or \
                board[0][0] == board[1][0] == board[2][0] == c or \
                board[0][1] == board[1][1] == board[2][1] == c or \
                board[0][2] == board[1][2] == board[2][2] == c or \
                board[0][2] == board[1][1] == board[2][0] == c or \
                board[0][0] == board[1][1] == board[2][2] == c:
            self.cell00.unbind('<Button-1>')
            self.cell01.unbind('<Button-1>')
            self.cell02.unbind('<Button-1>')
            self.cell10.unbind('<Button-1>')
            self.cell11.unbind('<Button-1>')
            self.cell12.unbind('<Button-1>')
            self.cell20.unbind('<Button-1>')
            self.cell21.unbind('<Button-1>')
            self.cell22.unbind('<Button-1>')
            return True


Main()
