# 13.6 (Count words) Write a program that counts the number of words in President
# Abraham Lincoln’s Gettysburg Address from http://cs.armstrong.edu/liang/data/
# Lincoln.txt.
import urllib.request

file = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")
data = file.read.decode()
data = data.split()
print("There are", len(data), "Words")
