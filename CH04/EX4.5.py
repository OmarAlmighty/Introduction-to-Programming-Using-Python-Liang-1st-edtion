# (Find future dates) Write a program that prompts the user to enter an integer for
# today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
# prompt the user to enter the number of days after today for a future day and display
# the future day of the week.

d = eval(input("Enter today's day: "))
n = eval(input("Enter the number of days elapsed since today: "))
res = (n + d) % 7
x = ""

if res == 0:
    x = "Sunday"
elif res == 1:
    x = "Monday"
elif res == 2:
    x = "Tuesday"
elif res == 3:
    x = "Wednesday"
elif res == 4:
    x = "Thursday"
elif res == 5:
    x = "Friday"
elif res == 6:
    x = "Saturday"

if d == 0:
    d = "Sunday"
elif d == 1:
    d = "Monday"
elif d == 2:
    d = "Tuesday"
elif d == 3:
    d = "Wednesday"
elif d == 4:
    d = "Thursday"
elif d == 5:
    d = "Friday"
elif d == 6:
    d = "Saturday"

print("Today is", d, "and the future day is", x)
