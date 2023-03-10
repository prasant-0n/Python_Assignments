# Difference between Sum of product of consecutive even digits except 2 and 6 and Sum of product of consecutive odd digits except 3 and 7 of any digit number

num = int(input('enter a number:'))

number = num
oddSum = 0
evenSum = 0
while num != 0:
    d1 = num % 10
    num //= 10
    d2 = num % 10
    # for odd
    if (d1 % 2 != 0 and d2 % 2 != 0):
        if (d1 != 3 and d1 != 7 and d2 != 3 and d2 != 7):
            oddSum += (d1*d2)
    # for Even
    if (d1 % 2 == 0 and d2 % 2 == 0):
        if (d1 != 2 and d1 != 6 and d2 != 2 and d2 != 6):
            evenSum += (d1*d2)
diff = 0
if oddSum > evenSum:
    diff = oddSum-evenSum
else:
    diff = evenSum-oddSum
print("Difference is ", diff)
