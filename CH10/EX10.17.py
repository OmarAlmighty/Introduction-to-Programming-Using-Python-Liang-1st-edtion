# 10.17 (Anagrams) Write a function that checks whether two words are anagrams.
# Two words are anagrams if they contain the same letters. For example, silent
# and listen are anagrams. The header of the function is:
# def isAnagram(s1, s2):
# (Hint: Obtain two lists for the two strings. Sort the lists and check if two lists
# are identical.)
# Write a test program that prompts the user to enter two strings and, if they
# are anagrams, displays is an anagram; otherwise, it displays is not an
# anagram.

def sort(lst):
    for i in range(len(lst) - 1, 0, -1):
        currentMax, currentMaxIndex = lst[i], i

        for j in range(i):
            if currentMax < lst[j]:
                currentMax, currentMaxIndex = lst[j], j

        if currentMaxIndex != i:
            lst[currentMaxIndex], lst[i] = lst[i], currentMax


def main():
    word1 = input("Enter first word: ")
    word1 = [x for x in word1]
    word2 = input("Enter second word: ")
    word2 = [x for x in word2]
    sort(word2)
    sort(word1)
    if word1 == word2:
        print("Anagrams")
    else:
        print("not anagrams")


main()
