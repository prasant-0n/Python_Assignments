# Write a python program to find 1st,2nd and 3rd largest and smallest numbers in
# a list 20 user defined values.

values = []
for i in range(1, 21):
    value = int(input(f"Enter a value:{i}- "))
    values.append(value)

largest = max(values)
values.remove(largest)
second_largest = max(values)
values.remove(second_largest)
third_largest = max(values)

smallest = min(values)
values.remove(smallest)
second_smallest = min(values)
values.remove(second_smallest)
third_smallest = min(values)

print("1st Largest Number:", largest)
print("2nd Largest Number:", second_largest)
print("3rd Largest Number:", third_largest)
print("1st Smallest Number:", smallest)
print("2nd Smallest Number:", second_smallest)
print("3rd Smallest Number:", third_smallest)
