#  Write a python program
# I. To add 'ing' at the end of a given string (length should be at least
# 3). If the given string already ends with 'ing' then add 'ly' instead. If
# the string length of the given string 5. is less than 3, leave it
# unchanged. Sample String: 'abc' Expected Result: 'abcing' Sample
# String: 'string' C 220.2 Expected Result: 'stringly'

# get input string from user
string = input("Enter a string: ")

# checking weather a string is at least 3 characters long
if len(string) >= 3:
    # checking for'ing'
    if string[-3:] == 'ing':
        string += 'ly'
    else:
        string += 'ing'

print("Modified String:", string)
