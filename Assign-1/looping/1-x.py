# X. Sum of product of consecutive prime digits of any digit number
num = int(input("enter the number:"))

number = num
primeSum = 0

while num != 0:
    d1 = num % 10
    num //= 10
    d2 = num % 10
    # check first number prime or not
    firstCount = 0
    secondCount = 0
    for i in range(d1):
        if i % d1 == 0:
            firstCount += 1
    for i in range(d2):
        if i % d2 == 0:
            secondCount += 1
    if firstCount == 1 and secondCount == 1:
        primeSum += (d1*d2)
print(f"Sum of product of consecutive Prime digits of {number} is: {primeSum}")
