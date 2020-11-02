# 13.5 (Replace text) Write a program that replaces text in a file. Your program should
# prompt the user to enter a filename, an old string, and a new string.

filename = input("Enter a filename: ").strip()
string = input("Enter the old string to be replaced: ")
new = input("Enter the new string to replace the old string: ")
file = open(filename, 'r')
data = ''
for line in file:
    data += line.replace(string, new)


# I will create a new file instead of writing on the same file for future exercises usage.
resFile = open('result', 'w')
resFile.write(data)
resFile.close()
print("done")