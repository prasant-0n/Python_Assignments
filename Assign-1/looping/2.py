# Write a python program to find sum of product of corresponding digits of two any digit number Such as n=1234 m=7896 output=6*4+9*3+8*2+7*1

num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
sum = 0
while num1 != 0 and num2 != 0:
    d1 = num1 % 10
    e1 = num2 % 10
    num1 //= 10
    num2 //= 10

    sum += (d1*e1)
print("The sum is:", sum)
