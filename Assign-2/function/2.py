# Wap to chech wheather a number is Armstrong number or not using defaunt arguments,required argument,kegyword araguments and function?

# Function to check if a number is an Armstrong number
def is_armstrong_number(num):
    num_str = str(num)
    order = len(num_str)
    sum_of_powers = sum([int(digit)**order for digit in num_str])
    return sum_of_powers == num


# Using default arguments to check if a number is an Armstrong number
default_num = input("enter a number - ")
default_is_armstrong = is_armstrong_number(default_num)
print(f"{default_num} is an Armstrong number (using default arguments):",
      default_is_armstrong)

# # Using required arguments to check if a number is an Armstrong number
# num = input("enter a number - ")
# required_is_armstrong = is_armstrong_number(num)
# print(f"{num} is an Armstrong number (using required arguments):",
#       required_is_armstrong)

# # Using keyword arguments to check if a number is an Armstrong number
# num = input("enter a number - ")
# kwargs_is_armstrong = is_armstrong_number(num=num)
# print(f"{num} is an Armstrong number (using keyword arguments):",
#       kwargs_is_armstrong)
