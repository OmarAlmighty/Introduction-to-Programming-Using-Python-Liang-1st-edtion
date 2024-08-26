# 5.26 (Sum a series) Write a program to sum the following series:

sum = 0
# As there was a computational error because the loop is running in linear,
# indeed it should increment by 2. But still you're a legend because you solved 5 years ago,
# but I'm doing in this modern era where there are so tools like gpt to assure solved problem
for i in range(1, 98, 2):
    sum += i / (i + 2)

print("Sum is", sum)
