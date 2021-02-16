# 15.24 (Number of files in a directory) Write a program that prompts the user to enter a
# directory and displays the number of files in the directory.
import os


def getNumberOfFiles(path):
    size = 0
    if not os.path.isfile(path):
        list = os.listdir(path)
        for i in range(len(list)):
            size += getNumberOfFiles(path + "\\" + list[i])
    else:
        size += 1

    return size


path = input("Enter a directory or a file: ").strip()
try:
    print("The number of files is " + str(getNumberOfFiles(path)))
except:
    print("File or directory does not exist")
