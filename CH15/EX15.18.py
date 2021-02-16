# 15.18 (Towers of Hanoi) Modify Listing 15.8, TowersOfHanoi.py, so that the program
# finds the number of moves needed to move n disks from tower A to tower B.
# (Hint: Use a global variable and increment it for every move.)

steps = 0


def main():
    n = eval(input("Enter number of disks: "))

    # Find the solution recursively
    print("The moves are:")
    moveDisks(n, 'A', 'B', 'C')
    print("The number of steps is: ", steps)


# The function for finding the solution to move n disks
#   from fromTower to toTower with auxTower
def moveDisks(n, fromTower, toTower, auxTower):
    global steps
    if n == 1:  # Stopping condition
        print("Move disk", n, "from", fromTower, "to", toTower)
        steps += 1
    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)
        print("Move disk", n, "from", fromTower, "to", toTower)
        steps += 1
        moveDisks(n - 1, auxTower, toTower, fromTower)


main()  # Call the main function
