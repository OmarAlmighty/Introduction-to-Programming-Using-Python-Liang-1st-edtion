# (Find the character of an ASCII code) Write a program that receives an ASCII
# code (an integer between 0 and 127) and displays its character. For example, if the
# user enters 97, the program displays the character a.

c = int(input("Enter an ASCII code: "))
c = chr(c)
print("The character is", c)
