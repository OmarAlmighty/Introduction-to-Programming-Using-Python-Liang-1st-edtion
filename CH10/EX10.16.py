# 10.16 (Bubble sort) Write a sort function that uses the bubble-sort algorithm. The
# bubble-sort algorithm makes several passes through the list. On each pass,
# successive neighboring pairs are compared. If a pair is in decreasing order,
# its values are swapped; otherwise, the values remain unchanged. The technique
# is called a bubble sort or sinking sort because the smaller values gradually
# “bubble” their way to the top and the larger values “sink” to the bottom.
# Write a test program that reads in ten numbers, invokes the function, and displays
# the sorted numbers.

def bubbleSort(lst):
    for i in range(len(lst)-1):
        for x in range(len(lst)-1):
            if lst[x] > lst[x+1]:
                lst[x], lst[x+1] = lst[x+1], lst[x]

def main():
    lst = input("Enter numbers: ").split()
    lst = [int(x) for x in lst]
    bubbleSort(lst)
    print(lst)

main()