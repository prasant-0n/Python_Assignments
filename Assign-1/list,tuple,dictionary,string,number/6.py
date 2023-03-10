# Write a python program to store names of 10 fruits in strings and sort in
# alphabetical order

# create a list of 10 fruits
fruits = []

for fruit in range(1, 11):
    name = input(f'enter fruit-{fruit} name:- ')
    fruits.append(name)

for i in range(len(fruits)):

    for j in range(i+1, len(fruits)):
        if fruits[i] > fruits[j]:
            fruits[i], fruits[j] = fruits[j], fruits[i]

print("Sorted List of Fruits are:", fruits)
