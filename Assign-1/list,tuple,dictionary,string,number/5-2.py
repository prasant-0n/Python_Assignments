# String: 'string' C 220.2 Expected Result: 'stringly'
# II. To get a string from a given string where all occurrences of its first
# char have been changed to '$', except the first char itself
# get input string from user
string = input("Enter a string: ")


first_char = string[0]

new_string = first_char

for char in string[1:]:
    if char == first_char:
        new_string += '$'
    else:
        new_string += char

print("Modified String:", new_string)
