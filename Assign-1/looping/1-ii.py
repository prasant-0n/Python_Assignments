# II. Sum of all even digits of any number
num1 = int(input("enter a number :"))
evenSum = 0

while num1 > 0:
    res = num1 % 10
    if res % 2 == 0:
        evenSum += res
    num1 //= 10

print("the sum of all even digit is: ", evenSum)
