# 10.5 (Print distinct numbers) Write a program that reads in numbers separated by a
# space in one line and displays distinct numbers (i.e., if a number appears multiple
# times, it is displayed only once). (Hint: Read all the numbers and store
# them in list1. Create a new list list2. Add a number in list1 to list2.
# If the number is already in the list, ignore it.)

n = input("Enter ten numbers: ")
l1 = [int(x) for x in n.split()]
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)

print("The distinct numbers are:",l2)
