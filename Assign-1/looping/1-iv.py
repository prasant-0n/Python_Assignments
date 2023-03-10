# IV. Sum of all prime digits

num = int(input("enter a number: "))
# digit =[int(x) for x in str(num)]
primeSum = 0

# print(digit)
while (num > 1):
    res = num % 10
    count = 0
    for x in range(2, num):
        if num % x == 0:
            count += 1
            break
    if count == 1:
        primeSum += res
    num //= 10

print("the sum Prime digit is:", primeSum);
