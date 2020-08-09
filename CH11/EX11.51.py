# 11.51 (Sort students) Write a program that prompts the user to enter the students’
# names and their scores on one line, and prints student names in increasing order
# of their scores. (Hint: Create a list. Each element in the list is a sublist with two
# elements: score and name. Apply the sort method to sort the list. This will sort
# the list on scores.)

lst = input("Enter students’ names and scores: ").split()
studs = []
for i in range(0, len(lst), 2):
    studs.append([lst[i], int(lst[i + 1])])

studs.sort(key=lambda x: x[1])
for x in studs:
    print(format(x[0], '8s'), end='')
    print(x[1])
