# 15.28 (Find words) Write a program that finds all the occurrences of a word in all the
# files under a directory, recursively. Your program should prompt the user to enter
# a directory name.

import os


def main():
    path = input("Enter a directory or a file: ").strip()
    s = input("Enter a string: ").strip()

    # Display the size
    try:
        findInFile(path, s)
    except:
        print("File or directory does not exist")


def findInFile(path, word):
    try:
        if not os.path.isfile(path):
            list = os.listdir(path)  # All files and subdirectories
            for i in range(len(list)):
                findInFile(list[i], word)  # Recursive call
        else:  # Base case
            findWord(path, word)
    except:
        print("Let it go")


def findWord(file, word):
    try:
        infile = open(file, "r")
        for line in infile:
            if line.find(word) > -1:
                print(file + ": " + line)
    except:
        print("Let is go")
    finally:
        infile.close()


main()
