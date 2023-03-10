# 1+x2/2! + x4/4!+ x6/6!+ ------+xn/n!

n = int(input("enter a  number:"))
x = int(input("enter a x number:"))

sum = 1


for i in range(2, n+1):
    # factorial
    fact = 1
    if i % 2 == 0:
        for j in range(1, i+1):
            fact *= j
        sum += pow(x, i)/fact


print('the OutPut is: ', sum)
