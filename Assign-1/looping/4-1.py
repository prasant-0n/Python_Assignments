# Write a python program to compute following series and take input x and n
# I. 1-x2/2! + x3/3!- x4/4!+ ------+x/n!
x = int(input('enter a x value:'))
n = int(input('enter a N value'))
sum = 1
# print("1+")
for i in range(2, n):
    # for factorial
    fact = 1
    for j in range(1, i):
        fact *= j

    # for Final result
    # print(f"x^{i
    sum += pow(x, i)//fact

print("the result output is: ", sum)
