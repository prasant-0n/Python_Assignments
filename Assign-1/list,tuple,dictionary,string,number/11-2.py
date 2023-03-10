# capitalize first and last character of each word in string

string = input("Enter a string: ")

words = string.split()

for i in range(len(words)):
    word = words[i]
    first_char = word[0].upper()
    last_char = word[-1].upper()
    middle_chars = word[1:-1]
    words[i] = first_char + middle_chars + last_char

new_string = " ".join(words)

print(new_string)
