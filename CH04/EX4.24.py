# 4.24 (Game: pick a card ) Write a program that simulates picking a card from a deck of
# 52 cards. Your program should display the rank (Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# Jack, Queen, King) and suit (Clubs, Diamonds, Hearts, Spades) of the card.
import random

shape = random.randint(1, 4)

if shape == 1:
    shape = "Clubs"
elif shape == 2:
    shape = "Diamonds"
elif shape == 3:
    shape = "Hearts"
elif shape == 4:
    shape = "Spades"

rank = random.randint(1, 13)

if rank == 1:
    rank = "Ace"
elif rank == 11:
    rank = "Jack"
elif rank == 12:
    rank = "Queen"
elif rank == 13:
    rank = "King"

print("The card you picked is the", rank, "of", shape)
