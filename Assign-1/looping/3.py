# Write a python program to find sum of product of corresponding even digits of first any digit number and corresponding odd digit of any digit number Such as n=1234 m=4567 output=4*7+2*5

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))
sum = 0
while num1 != 0 and num2 != 0:
    domyEven = num1 % 10
    domyOdd = num2 % 10
    num1 //= 10
    num2 //= 10
    if domyEven % 2 == 0 and domyOdd % 2 != 0:
        sum += (domyEven*domyOdd)
print("the Sum is:", sum)
