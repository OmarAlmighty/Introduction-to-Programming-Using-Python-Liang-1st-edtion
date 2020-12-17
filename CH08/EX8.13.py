# 8.13 (Longest common prefix) Write a method that returns the longest common prefix
# of two strings. For example, the longest common prefix of distance and
# disinfection is dis. The header of the method is:
# def prefix(s1, s2)
# If the two strings have no common prefix, the method returns an empty string.
# Write a main method that prompts the user to enter two strings and displays their
# common prefix.

def prefix(s1, s2):
    for i in range(len(s1)):
        s = s1[0:len(s1) - i]
        if str(s2).startswith(str(s)):
            return s

    return ""


def main():
    s1, s2 = input("Enter two strings: ").split()
    print(prefix(s1, s2))


main()
