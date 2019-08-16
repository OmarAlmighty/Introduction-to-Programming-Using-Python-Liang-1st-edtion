# (Population projection) Rewrite Exercise 1.11 to prompt the user to enter the
# number of years and displays the population after that many years.

numOfYears = eval(input("Enter the number of years: "))
population = int(312032486 + (((31536000 / 7) - (31536000 / 13) + (31536000 / 45)) * numOfYears))
print("The population in 5 years is", population)
