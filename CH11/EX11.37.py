# 11.37 (Simulation: self-avoiding random walk) Write a simulation program to show that
# the chance of getting dead-end paths increases as the grid size increases. Your program
# simulates lattices with sizes from 10 to 80. For each lattice size, simulate a
# self-avoiding random walk 10,000 times and display the probability of the deadend
# paths
from random import random

probs = [0] * 75
for N in range(10, 81):
    for time in range(10000):
        # lattice = 16 * [ 16 * [False]] # Wrong, each row will get the same list, i.e., id(lattice[0]) == id(
        # lattice[1])

        lattice = []  # No points in the lattice are traversed initially
        for i in range(N):
            list = N * [False]
            lattice.append(list)

        i = (N + 1) // 2
        j = (N + 1) // 2
        lattice[i][j] = True  # Starting point

        while 0 < i < N - 1 and 0 < j < N - 1:
            if lattice[i][j + 1] and lattice[i][j - 1] and lattice[i - 1][j] and lattice[i + 1][j]:
                probs[N - 10] += 1
                break

            r = random()
            if r < .25 and not lattice[i][j + 1]:
                lattice[i][j + 1] = True  # Right
                j += 1
            elif r < .50 and not lattice[i - 1][j]:
                lattice[i - 1][j] = True  # Down
                i -= 1

            elif r < .75 and not lattice[i][j - 1]:
                lattice[i][j - 1] = True  # Left
                j -= 1

            elif r < 1.00 and not lattice[i + 1][j]:
                lattice[i + 1][j] = True  # Up
                i += 1

probs = [(x * 100) / 10000 for x in probs]

for i in range(71):
    print('For a lattice of size', (i + 10), 'the probability of dead-end paths is', probs[i], '%')
