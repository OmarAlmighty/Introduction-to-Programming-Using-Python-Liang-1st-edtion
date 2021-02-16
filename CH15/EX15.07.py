# 15.7 (Fibonacci series) Modify Listing 15.2 so that the program finds the number of
# times the fib function is called. (Hint: Use a global variable and increment it
# every time the function is called.)

counter = 0


def fib(index):
    global counter
    counter += 1
    if index == 0:  # Base case
        return 0
    elif index == 1:  # Base case
        return 1
    else:  # Reduction and recursive calls
        return fib(index - 1) + fib(index - 2)


index = eval(input("Enter an index for a Fibonacci number: "))
fib(index)
print("The Fibonacci function is called", counter, "times")
