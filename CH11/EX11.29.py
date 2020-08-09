# 11.29 (Identical lists) The two-dimensional lists m1 and m2 are identical if they have the
# same contents. Write a function that returns True if m1 and m2 are identical, using
# the following header:
# def equals(m1, m2):
# Write a test program that prompts the user to enter two lists of integers and displays
# whether the two are identical.

def equals(m1, m2):
    for x in m1:
        if not(m2.__contains__(x)):
            return False

    return True

m1 = input("Enter list1: ").split()
m2 = input("Enter list2: ").split()

if equals(m1, m2):
    print("Two lists are identical")
else:
    print("Two lists are not identical")