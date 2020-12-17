# (Current time) Listing 2.7, ShowCurrentTime.py, gives a program that displays the
# current time in GMT. Revise the program so that it prompts the user to enter the
# time zone in hours away from (offset to) GMT and displays the time in the specified
# time zone.
import time

tzo = eval(input("Enter the time zone offset to GMT:"))
currentTime = time.time()
totalSeconds = int(currentTime)
currentSecond = totalSeconds % 60
totalMinutes = totalSeconds // 60
currentMintute = totalMinutes % 60
totalHours = totalMinutes // 60
currentHour = totalHours % 24
currentHour += tzo
print(currentHour, ":", currentMintute, ":", currentSecond)
