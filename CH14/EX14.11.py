# 14.11 (Count consonants and vowels) Write a program that prompts the user to enter a
# text filename and displays the number of vowels and consonants in the file. Use
# a set to store the vowels A, E, I, O, and U.

vowels = {'a', 'e', 'i', 'o', 'u'}
count_vowels = 0
count_consonants = 0
file = open(input("Enter filename: "))
lines = file.readlines()
for line in lines:
    for word in line.split():
        for c in word.lower():
            if c in vowels:
                count_vowels += 1
            else:
                count_consonants += 1

print("Total number of vowels =", count_vowels)
print("Total number of consonants =", count_consonants)
