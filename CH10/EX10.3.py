# 10.3 (Count occurrence of numbers) Write a program that reads some integers
# between 1 and 100 and counts the occurrences of each.

n = input("Enter integers between 1 and 100: ")
lst = [int(x) for x in n.split()]
counted = []
for x in lst:
    if x not in counted:
        c = lst.count(x)
        if c > 1:
            print(x, "occurs", c, "times")
        else:
            print(x, "occurs", c, "time")
        counted.append(x)
