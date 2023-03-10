# II. x-x3/3! + x5/5!- x7/7!+ ------+xn/n!
n = int(input("enter a  number:"))
x = int(input("enter a x number:"))

result = x
count = 0


for i in range(2, n+1):
    # factorial
    fact = 1
    for j in range(1, i+1):
        fact *= j
    result = result+pow(x, i)/fact if count % 2 == 0 else result-pow(x, i)/fact
    count += 1
print('the OutPut is: ', result)
