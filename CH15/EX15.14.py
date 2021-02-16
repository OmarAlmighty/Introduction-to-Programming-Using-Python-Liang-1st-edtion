# 15.14 (Occurrences of a specified character in a string) Rewrite Exercise 15.10 using a
# helper function to pass the substring of the high index to the function. The
# helper function header is:
# def countHelper(s, a, high):

def count(s, a):
    return countHelper(s, a, len(s) - 1)


def countHelper(s, a, high):
    result = 0
    if high >= 0:
        result = countHelper(s, a, high - 1) + (1 if s[high] == a else 0)

    return result


s, a = input("Enter a string and a character to count: ").split()
print("Character", a, "repeated", count(s.lower(), a.lower()), "times")
