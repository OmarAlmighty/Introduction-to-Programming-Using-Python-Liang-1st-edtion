# 4.17 (Game: scissor, rock, paper) Write a program that plays the popular scissor-rockpaper
# game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
# wrap a rock.) The program randomly generates a number 0, 1, or 2 representing
# scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or
# 2 and displays a message indicating whether the user or the computer wins, loses,
# or draws.
import random

c = random.randint(0, 2)
guess = int(input("scissor (0), rock (1), paper (2): "))
comp = ""
player = ""
isWon = False

if c == 0:
    comp = "scissor"
elif c == 1:
    comp = "rock"
else:
    comp = "paper"

if guess == 0:
    player = "scissor"
elif guess == 1:
    player = "rock"
else:
    player = "paper"

if guess == c:
    print("The computer is", comp, ". You are", player, ". It's a draw")
elif guess == 0 and c == 2:
    print("The computer is", comp, ". You are", player, ". You won")
elif c == 0 and guess == 2:
    print("The computer is", comp, ". You are", player, ". You lose")
elif guess > c and (guess != 0 and c != 2):
    print("The computer is", comp, ". You are", player, ". You won")
elif guess < c and (c != 0 and guess != 2):
    print("The computer is", comp, ". You are", player, ". You lose")

