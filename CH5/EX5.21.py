# 5.21 (Display numbers in a pyramid pattern) Write a nested for loop that displays the
# following output:

n = 9
x = n * 2
for i in range(1, n):
    s = n + x
    sp = str(s) + "s"
    print(format(" ", sp), end='')
    for j in range(0, i-1):
        print(format(2**j,"3d"), end='')

    for j in range(i-1,-1,-1):
        print(format(2 ** j, "3d"), end='')
    print()
    x-=3
