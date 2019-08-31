# 4.16 (Random character) Write a program that displays a random uppercase letter.
import random

n = random.randint(ord('A'), ord('Z'))
print(chr(n))
