# 4.13 (Financial application: compute taxes) Listing 4.7, ComputeTax.py, gives the
# source code to compute taxes for single filers. Complete Listing 4.7 to give the
# complete source code for the other filing statuses.
import sys

# Prompt the user to enter filing status
status = eval(input(
    "(0-single filer, 1-married jointly,\n" +
    "2-married separately, 3-head of household)\n" +
    "Enter the filing status: "))

# Prompt the user to enter taxable income
income = eval(input("Enter the taxable income: "))

# Compute tax
tax = 0

if status == 0:  # Compute tax for single filers
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 171550:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (income - 82250) * 0.28
    elif income <= 372950:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
            (income - 171550) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (82250 - 33950) * 0.25 + (171550 - 82250) * 0.28 + \
              (372950 - 171550) * 0.33 + (income - 372950) * 0.35
elif status == 1: # Compute tax for married file jointly
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10 + (income - 16700) * 0.15
    elif income <= 137050:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (income - 67900) * 0.25
    elif income <= 208850:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (137050 - 6700) * 0.25 + (income - 137050) * 0.28
    elif income <= 372950:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
            (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
            (income - 208850) * 0.33
    else:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + \
              (137050 - 67900) * 0.25 + (208850 - 137050) * 0.28 + \
              (372950 - 208850) * 0.33 + (income - 372950) * 0.35
elif status == 2: # Compute tax for married separately
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 68525:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (income - 33950) * 0.25
    elif income <= 104425:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + (income - 68525) * 0.28
    elif income <= 186475:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
            (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
            (income - 104425) * 0.33
    else:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + \
              (68525 - 33950) * 0.25 + (104425 - 68525) * 0.28 + \
              (186475 - 104425) * 0.33 + (income - 186475) * 0.35

elif status == 3: # Compute tax for head of household
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 11950 * 0.10 + (income - 11950) * 0.15
    elif income <= 117450:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (income - 45500) * 0.25
    elif income <= 190200:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + (income - 117450) * 0.28
    elif income <= 372950:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
            (117450 - 45500) * 0.25 + (104425 - 117450) * 0.28 + \
            (income - 192200) * 0.33
    else:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + \
              (117450 - 45500) * 0.25 + (192200 - 117450) * 0.28 + \
              (186475 - 192200) * 0.33 + (income - 372950) * 0.35
else:
    print("Error: invalid status")
    sys.exit()

# Display the result
print("Tax is", format(tax, ".2f"))
