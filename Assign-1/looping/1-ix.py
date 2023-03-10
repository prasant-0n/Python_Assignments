# IX. Sum of product of consecutive odd digits of any digit number

num = int(input("enter the number: "))
number = num
sum = 0
while num != 0:
    d1 = num % 10
    num //= 10
    d2 = num % 10
    if d1 % 2 != 0 and d2 % 2 != 0:
        sum += (d1*d2)

print("Sum of product of consecutive odd digits of %d is: %d" % (number, sum))
