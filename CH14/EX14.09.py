# 14.9 (Game: hangman) Write the hangman game with a graphics display, as shown in
# Figure 14.7. After seven misses, the program displays the word. The user can
# press the Enter key to continue to guess another word.
import random
from tkinter import *


class GUI:
    def __init__(self):
        self.WORDS = ('hello', 'welcome', 'play', 'dog', 'cat', 'telephone', 'television', 'satellite', 'computer')
        self.missed_letters = []
        self.word = self.WORDS[random.randint(0, len(self.WORDS) - 1)]
        self.str = list('*' * len(self.word))

        window = Tk()
        self.cnvs = Canvas(window, width=600, height=500)
        self.cnvs.pack()
        self.create_scene()

        self.cnvs.bind('<Key>', self.handle_input)
        self.cnvs.bind('<Return>', self.replay)
        self.cnvs.focus_set()

        window.mainloop()

    def handle_input(self, event):
        if event.char in self.word:
            self.cnvs.delete('txt')
            for i in range(len(self.word)):
                if self.word[i] == event.char:
                    self.str[i] = self.word[i]

                self.cnvs.delete('txt')
                txt = "Guess a word: " + "".join(self.str)
                self.cnvs.create_text(280, 380, text=txt, tag='txt')
        else:
            self.cnvs.delete('wrong')
            self.create_hangman(len(self.missed_letters))
            self.missed_letters.append(event.char)
            txt = "Missed letters: " + "".join(self.missed_letters)

        if "".join(self.str) == self.word or len(self.missed_letters)>6 :
            self.cnvs.delete('txt')
            self.cnvs.delete('wrong')
            txt = "The word is: " + "".join(self.word)
            self.cnvs.create_text(280, 380, text=txt, tag='txt')
            self.cnvs.create_text(280, 420, text='To continue the game press ENTER', tag='txt')

    def create_hangman(self, i):
        if i == 0:
            self.cnvs.create_line(260, 90, 260, 120, tag='man')  # create rope
        elif i == 1:
            self.cnvs.create_oval(230, 120, 290, 160, tag='man')  # create head
        elif i == 2:
            self.cnvs.create_line(235, 150, 150, 210, tag='man')  # create right arm
        elif i == 3:
            self.cnvs.create_line(285, 150, 370, 210, tag='man')  # create left arm
        elif i == 4:
            self.cnvs.create_line(260, 160, 260, 280, tag='man')  # create body
        elif i == 5:
            self.cnvs.create_line(260, 280, 200, 400, tag='man')  # create right leg
        else:
            self.cnvs.create_line(260, 280, 320, 400, tag='man')  # create left leg

    def create_scene(self):
        self.cnvs.create_arc(10, 430, 200, 630, start=30, extent=120, style=CHORD)
        self.cnvs.create_line(105, 430, 105, 90)
        self.cnvs.create_line(105, 90, 260, 90)

        txt = "Guess a word: " + ('*' * len(self.word))
        self.cnvs.create_text(280, 380, text=txt, tag='txt')

    def replay(self, event):
        self.cnvs.delete('man')
        self.cnvs.delete('txt')
        self.word = self.WORDS[random.randint(0, len(self.WORDS) - 1)]
        self.str = list('*' * len(self.word))
        txt = "Guess a word: " + ('*' * len(self.word))
        self.cnvs.create_text(280, 380, text=txt, tag='txt')
        self.missed_letters = []
GUI()
