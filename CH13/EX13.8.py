# 13.8 (Encrypt files) Encode the file by adding 5 to every byte in the file. Write a program
# that prompts the user to enter an input filename and an output filename and
# saves the encrypted version of the input file to the output file.

infile = input("Enter input filename: ")
outfile = input("Enter output filename: ")

source = open(infile, 'r')
destination = open(outfile, 'w')
res = ''

data = source.read()
for i in range(len(data)):
    res += chr(ord(data[i])+5)


destination.write(res)
destination.close()