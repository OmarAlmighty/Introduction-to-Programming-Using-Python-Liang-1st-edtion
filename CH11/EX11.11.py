# 11.11 (Game: nine heads and tails) Nine coins are placed in a matrix with some
# face up and some face down. You can represent the state of the coins with the values
# 0 (heads) and 1 (tails). Here are some examples:
# 0 0 0   1 0 1   1 1 0   1 0 1   1 0 0
# 0 1 0   0 0 1   1 0 0   1 1 0   1 1 1
# 0 0 0   1 0 0   0 0 1   1 0 0   1 1 0
# Each state can also be represented using a binary number. For example, the preceding
# matrices correspond to the numbers:
# 000010000 101001100 110100001 101110100 100111110
# There are a total of 512 possibilities. So, you can use the decimal numbers 0, 1, 2,
# 3, ..., and 511 to represent all states of the matrix. Write a program that prompts
# the user to enter a number between 0 and 511 and displays the corresponding
# 3 * 3 matrix with the characters H and T.
# The user entered 7, which corresponds to 000000111. Since 0 stands for H and 1 for T, the output is correct.

def dec_to_bin(num):
    bin = []
    while num > 0:
        bin.append(num % 2)
        num = num // 2

    while len(bin) < 9:
        bin.append(0)

    bin.reverse()
    return bin


def print_matrix(mat):
    for i in range(len(mat)):
        if mat[i] == 0:
            print('H', end=' ')
        else:
            print('T', end=' ')

        if (i + 1) % 3 == 0:
            print()


num = int(input("Enter a number between 0 and 511: "))
mat = dec_to_bin(num)
print_matrix(mat)
