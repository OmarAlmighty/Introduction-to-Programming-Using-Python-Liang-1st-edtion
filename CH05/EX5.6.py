# 5.6 (Conversion from miles to kilometers and kilometers to miles) Write a program
# that displays the following two tables side by side (note that 1 mile is 1.609 kilometers
# and that 1 kilometer is .621 mile):

MILES_TO_KILOMETRE = 1.609
KILOMETRE_TO_MILE = 0.621
mile = 1
kilometre = 20
print(format("Mile", "8s"), format("Kilometre", "8s"), format(" ", "2s"), format("|", "5s")
      , format("Kilometre", "12s"), "Mile")

while mile < 11:
    miles = kilometre * KILOMETRE_TO_MILE
    kilometres = mile * MILES_TO_KILOMETRE

    print(format(mile, "-2.0f"), format(kilometres, "12.3f"), format(" ", "5s"), "|"
          , format(kilometre, "6.0f"), format(miles, "16.3f"))
    mile += 1
    kilometre += 5
