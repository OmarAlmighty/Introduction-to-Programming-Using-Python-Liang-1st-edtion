# 14.1 (Display keywords) Revise Listing 14.4 CountKeywords.py to display the keywords
# in a Python source file as well as to count the number of the keywords.

import os.path
import sys


def main():
    keyWords = {"and": 0, "as": 0, "assert": 0, "break": 0, "class": 0,
                "continue": 0, "def": 0, "del": 0, "elif": 0, "else": 0,
                "except": 0, "False": 0, "finally": 0, "for": 0, "from": 0,
                "global": 0, "if": 0, "import": 0, "in": 0, "is": 0, "lambda": 0,
                "None": 0, "nonlocal": 0, "not": 0, "or": 0, "pass": 0, "raise": 0,
                "return": 0, "True": 0, "try": 0, "while": 0, "with": 0, "yield": 0}

    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename):  # Check if target file exists
        print("File", filename, "does not exist")
        sys.exit()

    infile = open(filename, "r")  # Open files for input

    text = infile.read().split()  # Read and split words from the file

    count = 0
    for word in text:
        if word in keyWords:
            count += 1
            keyWords[word] += 1

    print("The number of key words:", count)
    for w in keyWords:
        if keyWords[w] > 0:
            print(w, ":", keyWords[w])


main()
