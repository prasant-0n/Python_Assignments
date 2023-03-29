# find and count number of words starts and ends with vowels in a
# string of multiple words


input_string = input("enter a string - ")

# Split the input string into individual words
words = input_string.split()

# Initialize counters
starts_with_vowel = 0
ends_with_vowel = 0

# Loop through each word in the words list
for word in words:

    # Check if the word starts with a vowel
    if word[0] in "aeiouAEIOU":
        starts_with_vowel += 1

    # Check if the word ends with a vowel
    if word[-1] in "aeiouAEIOU":
        ends_with_vowel += 1

# Print the results
print("Number of words that start with a vowel:", starts_with_vowel)
print("Number of words that end with a vowel:", ends_with_vowel)
