# x-x3/3! + x5/5!- x7/7!+ x11/11!- -----+xn/n!
n = int(input("enter a  number:"))
x = int(input("enter a x number:"))

result = 0
total = 0
finalcount = 0

for i in range(2, n+1):
    count = 0
    for j in range(1, n+1):
        if j % 2 == 0 and j != 1 and j != i:
            count += 1
    if count == 1:
        # finding factorial of a i
        fact = 1
        for k in range(1, i+1):
            fact *= k
        # sum += pow(x, i)/fact
        result = pow(x, i)/fact
        total = total-result if finalcount % 2 == 0 else total+result
        finalcount += 1
print('output is ', total)
