# 10.19 (Game: bean machine) The bean machine, also known as a quincunx or the
# Galton box, is a device for statistics experiments named after English scientist
# Sir Francis Galton. It consists of an upright board with evenly spaced nails (or
# pegs) in a triangular pattern, as shown in Figure 10.15.
# Balls are dropped from the opening of the board. Every time a ball hits a nail,
# it has a 50% chance of falling to the left or to the right. The piles of balls are
# accumulated in the slots at the bottom of the board.Write a program that simulates the bean machine. Your program should
# prompt the user to enter the number of the balls and the number of the slots in
# the machine. Simulate the falling of each ball by printing its path. For example,
# the path for the ball in Figure 10.15b is LLRRLLR and the path for the ball in
# Figure 10.15c is RLRRLRR. Display the final buildup of the balls in the slots
# in a histogram.
# (Hint: Create a list named slots. Each element in slots stores the number
# of balls in a slot. Each ball falls into a slot via a path. The number of Rs in a
# path is the position of the slot where the ball falls. For example, for the path
# LRLRLRR, the ball falls into slots[4], and for the path is RRLLLLL, the
# ball falls into slots[2].)
import random

balls = 5  # eval(input("Enter the number of balls to drop: "))
slots = 7  # eval(input("Enter the number of slots in the bean machine: "))
l = 0
r = 0
lst = [0] * balls

for b in range(1, balls + 1):
    for s in range(1, slots + 1):
        x = random.randint(1, s * 2)
        if 1 <= x <= s:
            print("L", end="")
            l += 1
        else:
            print("R", end="")
            r += 1
    lst[b - 1] = r
    l = 0
    r = 0
    print()

print(lst)
# in slot X there are Y balls above each other, means that if i have, for example, in the third slot i have 2 balls
# and in the fourth slot i have 2 balls, that means have two balls in the same row one in the third column(slot) and the
# other in the fourth column(slot).
end_location = [0] * slots
for i in range(len(lst)):
    end_location[lst[i]] += 1

print("\n")
for v in reversed(range(1, max(end_location) + 1)):
    print(''.join('O' if x >= v else ' ' for x in end_location))

# refer to this https://stackoverflow.com/questions/35877175/the-bean-machine-function-python
