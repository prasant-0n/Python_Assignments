# categories the password as low medium and high low – only numbers or alphabets and length less than 8
# medium - number and alphabets and length more than 8 string - number, alphabet and special character should present
# and length should be greater than 8

password = input("Enter a password: ")

if password.isalnum() and len(password) < 8:
    print("Password category: low")

elif password.isalnum() and len(password) >= 8:
    print("Password category: medium")

elif not password.isalnum() and len(password) >= 8:
    print("Password category: high")

else:
    print("Invalid password")
