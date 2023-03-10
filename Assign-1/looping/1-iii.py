# III. Sum of all odd digits of any number

num = int(input("enter a number:"))
Oddsum = 0
while (num > 0):
    res = num % 10
    if res % 2 != 0:
        Oddsum += res
    num //= 10
print("the sum of Odd digit is:", Oddsum)
