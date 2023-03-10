# Find kth digit from frontside or back side of any digits number and find its poistional value

num = int(input("Enter the number: "))
choice = input(
    "Enter the choice to choose the number from f for Front side and b for Back side: ")
k = int(input("Enter the position: "))

temp = num
length = 0
while temp != 0:
    length += 1
    temp //= 10

if length < k:
    print("Index is out of range!!")
    exit()

temp = num

positionValue = 1
placeValue = 0

if choice.lower() in ["f", "front"]:
    positionValue = 0
    placeValue = 0
    for count in range(1, k+1):
        positionValue = 1 if positionValue == 0 else positionValue * 10
        placeValue = temp % 10
        temp //= 10
    print(
        f"The kth digit from the front is {placeValue} having the place value {placeValue * positionValue}")

elif choice.lower() in ["b", "back"]:
    t = num
    temp = 0
    positionValue = 1
    while t > 0:
        temp = (temp * 10) + (t % 10)
        t //= 10
        positionValue *= 10
    placeValue = 0
    for count in range(1, k+1):
        positionValue //= 10
        placeValue = temp % 10
        temp //= 10
    print(
        f"The kth digit from the back is {placeValue} having the place value {placeValue * positionValue}")

else:
    print("Invalid Input!!!")
