# 5.5 (Conversion from kilograms to pounds and pounds to kilograms) Write a program
# that displays the following two tables side by side (note that 1 kilogram is 2.2
# pounds and that 1 pound is .45 kilograms):
# Kilograms Pounds | Pounds Kilograms
# 1 2.2 | 20 9.09
# 3 6.6 | 25 11.36
# ...
# 197 433.4 | 510 231.82
# 199 437.8 | 515 235.09

pound = 20
kilogram = 1
KILOGRAM_TO_POUND = 2.2
POUND_TO_KILOGRAM = 0.45
print(format("Kilograms", "15s"), format("Pounds", "8s"), format("|", "5s"), format("Pounds", "12s"), "Kilograms")
while kilogram < 200:
    pounds = kilogram * KILOGRAM_TO_POUND
    kilograms = pound * POUND_TO_KILOGRAM
    print(kilogram, format(pounds, "18.1f"), format(" ", "3s"),
          format("|", "2s"), format(pound, "6.0f"), format(kilograms, "16.2f"))
    kilogram += 2
    pound += 5
