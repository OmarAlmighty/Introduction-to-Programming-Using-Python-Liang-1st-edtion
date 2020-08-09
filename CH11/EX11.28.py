# 11.28 (Strictly identical lists) The two-dimensional lists m1 and m2 are strictly identical
# if their corresponding elements are equal. Write a function that returns True if m1
# and m2 are strictly identical, using the following header:
# def equals(m1, m2):
# Write a test program that prompts the user to enter two lists of integers and
# displays whether the two are strictly identical.

def main():
    m1 = input("Enter list1: ").split()
    m2 = input("Enter list2: ").split()

    if equals(m1, m2):
        print("Two lists are strictly identical")
    else:
        print("Two lists are not strictly identical")


def equals(m1, m2):
    for i in range(len(m1)):
        if m1[i] != m2[i]: return False

    return True


main()