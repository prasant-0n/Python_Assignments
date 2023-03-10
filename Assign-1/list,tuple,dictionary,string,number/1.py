# rite a python program to create a list of prime numbers as per given range

num1 = int(input('enter first number:'))
num2 = int(input('enter last  number:'))
list = []
for i in range(num1, num2):
    count = 0
    for j in range(1, i):
        if i % j == 0:
            count += 1
    if count == 1:
        # prime = i
        list.append(i)

print(f'the prime nunbers in the range{num1} and {num2} are {list}')
