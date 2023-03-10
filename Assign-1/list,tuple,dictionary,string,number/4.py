num = int(input('enter a numbern of terms: '))

fib_list = [0, 1]
a, b = 0, 1

for i in range(2, num):
    c = a+b
    fib_list.append(c)
    a, b = b, c

# printing the fibbonacy series
for i in fib_list:
    print(i)
