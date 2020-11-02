# 13.2 (Count characters, words, and lines in a file) Write a program that will count the
# number of characters, words, and lines in a file. Words are separated by a whitespace
# character. Your program should prompt the user to enter a filename.

filename = input("Enter a filename: ").strip()
file = open(filename, 'r')

lines = 0
words = 0
chars = 0

for line in file:
    lines += 1
    words += len(line.split())
    for c in line:
        if c != ' ':
            chars += 1

print(chars, "characters")
print(words, "words")
print(lines, "Lines")
