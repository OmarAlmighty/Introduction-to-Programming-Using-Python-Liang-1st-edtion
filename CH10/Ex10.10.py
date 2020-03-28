# 10.10 (Reverse a list) The reverse function in Section 10.8 reverses a list by copying it
# to a new list. Rewrite the function that reverses the list passed in the argument and
# returns this list. Write a test program that prompts the user to enter a list of numbers,
# invokes the function to reverse the numbers, and displays the numbers.

def reverse(lst):
    for i in range(len(lst)//2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]

def main():
    lst = input("Enter numbers: ").split()
    lst = [int(x) for x in lst]
    reverse(lst)
    print(lst)

main()
