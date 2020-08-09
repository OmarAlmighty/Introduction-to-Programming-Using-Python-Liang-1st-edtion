def f(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            for k in range(len(m[j])):
                m[i][j][k] += 1
def printM(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            for k in range(len(m[j])):
                print(m[i][j][k], end = "")
        print()

m = [[[0, 0], [0, 1]], [[0, 0], [0, 1]]]

printM(m)
f(m)
printM(m)