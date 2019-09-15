# 5.20 (Display four patterns using loops) Use nested loops that display the following
# patterns in four separate programs:

N = 7
# Pattern A
for i in range(1, N):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n")

# Patten B
x = N
for i in range(1, N):
    for j in range(1, x):
        print(j, end=" ")
    print()
    x -= 1

print("\n")

# Pattern C
for i in range(1, N):
    for j in range(N, i - 1, -1):
        print(" ", end=' ')
    for k in range(i, 0, -1):
        print(k, end=' ')
    print()

print("\n")

# Pattern D
y = N
for i in range(1, N):
    for j in range(y - 1, 0, -1):
        print(j, end=" ")
    print()
    y -= 1
