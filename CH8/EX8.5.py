# 8.5 (Occurrences of a specified string) Write a function that counts the occurrences of a
# specified non-overlapping string s2 in another string s1 using the following header:
# def count(s1, s2):
# For example, count("system error, syntax error", "error") returns
# 2. Write a test program that prompts the user to enter two strings and displays the
# number of occurrences of the second string in the first string.

def count(s1, s2):
    counter = 0
    s1 = s1 + ' '
    while len(s1) > 0:
        s = s1[0: s1.index(' ')]
        s = s[0:len(s2)]
        if s == s2:
            counter += 1
        s1 = s1[s1.index(' ')+1: len(s1)]
    return counter


def main():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    c = count(str1, str2)
    print("String", str2, "is occurred", c, "times in", str1)


main()
