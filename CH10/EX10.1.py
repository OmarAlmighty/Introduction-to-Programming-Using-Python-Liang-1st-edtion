# 10.1 (Assign grades) Write a program that reads a list of scores and then assigns grades
# based on the following scheme:
# The grade is A if score is >= best – 10.
# The grade is B if score is >= best – 20.
# The grade is C if score is >= best – 30.
# The grade is D if score is >= best – 40.
# The grade is F otherwise.

scores = input("Enter scores: ")
lst = [int(s) for s in scores.split()]
best = max(lst)
for x in range(len(lst)):
    if lst[x] >= best - 10:
        print("Student", x, "score is", lst[x], "and grade is A")
    elif lst[x] >= best - 20:
        print("Student", x, "score is", lst[x], "and grade is B")
    elif lst[x] >= best - 30:
        print("Student", x, "score is", lst[x], "and grade is C")
    elif lst[x] >= best - 40:
        print("Student", x, "score is", lst[x], "and grade is D")
    else:
        print("Student", x, "score is", lst[x], "and grade is F")
