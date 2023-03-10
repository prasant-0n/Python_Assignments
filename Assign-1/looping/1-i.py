num = int(input("enter a number :"))
num1 = num
sum = 0
while num1 > 0:
    res = num1 % 10
    sum += res
    num1 //= 10

print("the sum of all digit is: ", sum)
