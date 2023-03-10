# Difference between average of all even digits except divisible by 4 and avearge of all odd digits except divisble by 3


num = int(input("enter a number:"))

Evensum = 0
Oddsum = 0

while (num > 0):
    rem = num % 10
    if rem % 2 == 0 and rem % 4 != 0:
        Evensum += rem

    elif rem % 2 != 0 and rem % 3 != 0:
        Oddsum += rem
    num//=10;

if Evensum < Oddsum:
    print("Difference is :", Oddsum-Evensum)
elif Evensum > Oddsum:
    print("Diffrence is :", Evensum-Oddsum)
