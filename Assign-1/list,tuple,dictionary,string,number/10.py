# Write a python program to create a tuple of constants values like pi and
# exponent and use them to find area and perimeter of circle

import math


constants = (math.pi, math.e)


radius = float(input("Enter the radius of the circle: "))

area = constants[0] * radius ** 2
perimeter = 2 * constants[0] * radius

# print the results
print(f"The area of the circle is {area:.2f}")
print(f"The perimeter of the circle is {perimeter:.2f}")
