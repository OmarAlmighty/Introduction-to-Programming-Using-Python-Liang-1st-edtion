# 14.8 (Display nonduplicate words in ascending order) Write a program that prompts
# the user to enter a text file, reads words from the file, and displays all the nonduplicate
# words in ascending order.

filename = open(input("Enter text file: "))

lines = filename.readlines()
lines = [line.lower() for line in lines]

words = set()
for line in lines:
    for word in line.split():
        words.add(word)

i = 0
for x in words:
    print(x, end=' ')
    i += 1
    if i == 10:
        print()
        i = 0
