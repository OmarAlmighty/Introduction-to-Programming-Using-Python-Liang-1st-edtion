# 5.9 (Financial application: compute future tuition) Suppose that the tuition for a university
# is $10,000 this year and increases 5% every year. Write a program that
# computes the tuition in ten years and the total cost of four years’ worth of tuition
# starting ten years from now.

tuition = 10000
total = 0
for i in range(1, 15):
    tuition += tuition * 1.05
    if i == 10:
        print("The cost of tuition in 10 years is $", format(tuition, ".2f"))
    if i > 10:
        total = total + tuition
