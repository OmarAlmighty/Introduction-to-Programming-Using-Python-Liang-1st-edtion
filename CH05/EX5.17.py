# 5.17 (Display the ASCII character table) Write a program that displays the characters
# in the ASCII character table from ! to ~. Display ten characters per line. The characters
# are separated by exactly one space.

counter = 0
for i in range(ord('!'), ord('~')):
    if counter == 10:
        print()
        counter = 0
    print(chr(i), end=" ")
    counter+=1
