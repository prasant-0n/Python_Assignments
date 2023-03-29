# create a list to store unique character in string and another listto store frequency of repeatation of unique character available in first list in the string
# string
# Input string
input_string = input("enter a string:- ")

# Initialize empty lists
unique_chars = []
char_freq = []

# Loop through each character in the string
for char in input_string:

    # If the character is not already in unique_chars, add it and set its frequency to 1
    if char not in unique_chars:
        unique_chars.append(char)
        char_freq.append(1)

    # If the character is already in unique_chars, increment its frequency in char_freq
    else:
        index = unique_chars.index(char)
        char_freq[index] += 1

# Print the results
print("Unique characters:", unique_chars)
print("Character frequency:", char_freq)
