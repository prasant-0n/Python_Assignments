# # WAP to do following using string
#         a) Check whether a string is palindrome or not

string = input("Enter a string: ")

string = string.replace(" ", "").lower()

reverse_string = string[::-1]

if string == reverse_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
