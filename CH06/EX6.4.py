# 6.4 (Display an integer reversed) Write the following function to display an integer in
# reverse order:
# def reverse(number):
# For example, reverse(3456) displays 6543. Write a test program that prompts
# the user to enter an integer and displays its reversal.

def reverse(number):
    num = ""
    while number > 0:
        n1 = number % 10
        num = num + str(n1)
        number = number // 10

    return num


num = eval(input("Enter a number: "))
print("The reverse of", num, "is", reverse(num))
