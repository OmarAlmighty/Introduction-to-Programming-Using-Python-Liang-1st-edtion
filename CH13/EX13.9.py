# 13.9 (Decrypt files) Suppose a file is encrypted using the scheme in Exercise 13.8.
# Write a program to decode an encrypted file. Your program should prompt the
# user to enter an input filename and an output filename and should save the unencrypted
# version of the input file to the output file.

infile = input("Enter input filename: ")
outfile = input("Enter output filename: ")

source = open(infile, 'r')
destination = open(outfile, 'w')
res = ''

data = source.read()
for i in range(len(data)):
    res += chr(ord(data[i]) - 5)

destination.write(res)
destination.close()
