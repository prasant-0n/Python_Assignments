# Write a python program to find difference between average of all even
# numbers except divisible by 4 and average of all odd numbers except
# divisible by 5 in a list of user defined 20 values?

num = []
diff = 0
Odd_avg, Even_avg = 0, 0
Even_sum, Odd_sum = 0, 0
Even_count, Odd_count = 0, 0


for n in range(1, 21):
    n = int(input(f'enter a number-{n}: ',))
    num.append(n)


for n in num:
    if n % 2 == 0 and n % 4 != 0:
        Even_sum += n
        Even_count += 1
    if n % 2 != 0 and n % 5 != 0:
        Odd_sum += n
        Odd_count += 1

Even_avg = Even_sum/Even_count
Odd_avg = Odd_sum/Odd_count

if Even_avg > Odd_avg:
    diff = Even_avg-Odd_avg
else:
    diff = Odd_avg-Even_avg

print(f'the difference is: {diff}')
