# VII. Sum of product of consecutive digits of any digit number

num = input("Enter a number: ")
sum = 0

for i in range(len(num)-1):
    sum += int(num[i]) * int(num[i+1])

print("Sum of product of consecutive digits:", sum)
