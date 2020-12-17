# 8.2 (Check substrings) You can check whether a string is a substring of another string
# by using the find method in the str class. Write your own function to implement
# find. Write a program that prompts the user to enter two strings and then checks
# whether the first string is a substring of the second string.

def main():
    s1 = input("First string: ")
    s2 = input("Second string: ")
    f = find(s1, s2)
    if f == -1:
        print(s1, "is not substring of", s2)
    else:
        print(s1, "is substring of", s2, "at index", f)


def find(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    start = 0
    while l1 <= l2:
        if s1 != s2[start:start + l1]:
            start += 1
            l2 -= 1
        else:
            return start
    return -1


main()
