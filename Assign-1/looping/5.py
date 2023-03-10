# Write a python program compute following series and take a numbers num as input
#  x-x3/3! + x5/5!-x7/7!+------+xn/n!
#  where x=sum of all even digits except 2 and 8
#  and n= sum of all odd digits except 1 and 3

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
