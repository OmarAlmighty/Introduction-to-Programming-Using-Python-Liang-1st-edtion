# (Convert milliseconds to hours, minutes, and seconds) Write a function that converts
# milliseconds to hours, minutes, and seconds using the following header:
# def convertMillis(millis):
# The function returns a string as hours:minutes:seconds. For example,
# convertMillis(5500) returns the string 0:0:5, convertMillis(100000)
# returns the string 0:1:40, and convertMillis(555550000) returns the string
# 154:19:10.
# Write a test program that prompts the user to enter a value for milliseconds and
# displays a string in the format of hours:minutes:seconds.

def convertMillis(millis):
    totalSeconds = millis // 1000

    totalMin = totalSeconds // 60

    totalHours = totalMin // 60

    return totalSeconds % 60, totalMin % 60, totalHours


def main():
    s, m, h = convertMillis(int(input("Enter millis: ")))
    print(h, ":", m, ":", s)


main()
