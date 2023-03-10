# Write a python program to find repeated numbers as well as frequency of
# repetition of numbers in a list of 20 user defined values?

values = []
for i in range(1, 21):
    value = int(input(f"Enter a value-{i}: "))
    values.append(value)

repeated_numbers = []
frequency_dict = {}

for value in values:
    if value in frequency_dict:
        frequency_dict[value] += 1
        if value not in repeated_numbers:
            repeated_numbers.append(value)
    else:
        frequency_dict[value] = 1


print("Repeated Numbers:", repeated_numbers)
for number in repeated_numbers:
    frequency = frequency_dict[number]
    print(f"Frequency of {number}: {frequency}")
