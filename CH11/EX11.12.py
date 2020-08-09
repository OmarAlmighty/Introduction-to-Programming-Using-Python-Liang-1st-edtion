# 11.12 (Financial application: compute tax) Rewrite Listing 4.7, ComputeTax.py, using
# lists. For each filing status, there are six tax rates. Each rate is applied to a certain
# amount of taxable income. For example, from the taxable income of $400,000 for
# a single filer, $8,350 is taxed at 10%, (33,950 – 8,350) at 15%, (82,250 – 33,950)
# at 25%, (171,550 – 82,250) at 28%, (372,950 – 171,550) at 33%, and (400,000 –
# 372,950) at 35%. The six rates are the same for all filing statuses, which can be
# represented in the following list:
# rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]
# The brackets for each rate for all the filing statuses can be represented in a twodimensional
# list as follows:
# brackets = [
# [8350, 33950, 82250, 171550, 372950], # Single filer
# [16700, 67900, 137050, 208850, 372950], # Married jointly
# [8350, 33950, 68525, 104425, 186475], # Married separately
# [11950, 45500, 117450, 190200, 372950] # Head of household
# ]
# Suppose the taxable income is $400,000 for single filers. The tax can be computed
# as follows:
# tax = brackets[0][0] * rates[0] +
# (brackets[0][1] – brackets[0][0]) * rates[1] +
# (brackets[0][2] – brackets[0][1]) * rates[2] +
# (brackets[0][3] – brackets[0][2]) * rates[3] +
# (brackets[0][4] – brackets[0][3]) * rates[4] +
# (400000 – brackets[0][4]) * rates[5]

def main():
    status = eval(input("(0-single filer, 1-married jointly,\n" +
                        "2-married separately, 3-head of household)\n" +
                        "Enter the filing status: "))

    # Prompt the user to enter taxable income
    income = eval(input("Enter the taxable income: "))

    # Compute and display the result
    print("Tax is", format(computeTax(status, income), "7.2f"))


def computeTax(status, income):
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    brackets = [
        [8350, 33950, 82250, 171550, 372950],  # Single filer
        [16700, 67900, 137050, 20885, 372950],  # Married jointly
        [8350, 33950, 68525, 104425, 186475],  # Married separately
        [11950, 45500, 117450, 190200, 372950]  # Head of household
    ]

    tax = 0  # Tax to be computed

    # Compute tax in the first bracket
    if income <= brackets[status][0]:
        return income * rates[0]  # Done
    else:
        tax = brackets[status][0] * rates[0]

        # Compute tax in the 2nd, 3rd, 4th, and 5th brackets, if needed
        for i in range(1, len(brackets[0])):
            if income > brackets[status][i]:
                tax += (brackets[status][i] - brackets[status][i - 1]) * rates[i]
            else:
                tax += (income - brackets[status][i - 1]) * rates[i]
                return tax  # Done

            # Compute tax in the last (i.e., 6th) bracket
            return tax + (income - brackets[status][4]) * rates[5]


main()
