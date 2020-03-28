# 10.30 (Culture: Chinese Zodiac) Simplify Listing 4.5, ChineseZodiac.py, using a list
# of strings to store the animals’ names.

temp = year = eval(input("Enter a year: "))

if year >= 1900:
    year -= 1900
else:
    year = 12 - (1900 - year) % 12

animals = ["rat", "ox", "tiger", "rabbit", "dragon",
               "snake", "horse", "sheep", "monkey", "rooster", "dog", "pig"]

print(temp, "is", animals[year % 12])


