# 8.12 (Bioinformatics: find genes) Biologists use a sequence of letters A, C, T, and G to
# model a genome. A gene is a substring of a genome that starts after a triplet ATG
# and ends before a triplet TAG, TAA, or TGA. Furthermore, the length of a gene
# string is a multiple of 3 and the gene does not contain any of the triplets ATG, TAG,
# TAA, and TGA. Write a program that prompts the user to enter a genome and displays
# all genes in the genome. If no gene is found in the input sequence, the program
# displays no gene is found.

def findGen(genome):
    found = False
    for i in range(len(genome)):
        startInd = str(genome).find("ATG")
        if startInd == -1:
            break
        endInd1, endInd2, endInd3 = \
            str(genome).find("TAG"), str(genome).find("TAA"), str(genome).find("TGA")
        if endInd1 == -1:
            endInd1 = len(genome) * 2
        if endInd2 == -1:
            endInd2 = len(genome) * 2
        if endInd3 == -1:
            endInd3 = len(genome) * 2
        endInd = min(endInd1, endInd2, endInd3)
        gen = str(genome)[startInd + 3:endInd]
        if len(gen) % 3 == 0:
            print(gen)
            found = True
        genome = genome[endInd + 3:len(genome)]

    if not found:
        print("No genes found")


def main():
    g = input("Enter a genome string: ")
    findGen(g)


main()
