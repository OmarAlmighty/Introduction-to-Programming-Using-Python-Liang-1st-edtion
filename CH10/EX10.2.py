# 10.2 (Reverse the numbers entered) Write a program that reads a list of integers and
# displays them in the reverse order in which they were read.

n = input("Enter numbers: ")
lst = [int(s) for s in n.split()]
lst.reverse()
print(lst)