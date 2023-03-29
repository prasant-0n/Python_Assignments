# Wap to create a list of prime Fibonacci series between user defined range
# and default range is 10 to 50 using defaunt arguments,required argument,kegyword araguments and function?

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Function to generate Fibonacci series up to a given limi


def fibonacci_series(limit):
    fib_series = [0, 1]
    while fib_series[-1] <= limit:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[1:-1]

# Function to generate a list of prime Fibonacci series


def prime_fibonacci(start, end=None):
    if end is None:
        end = 50
    fib_series = fibonacci_series(end)
    prime_fib_list = [n for n in fib_series if is_prime(
        n) and start <= n <= end]
    return prime_fib_list


# Using default arguments to generate a list of prime Fibonacci series between 10 and 50
default_prime_fib_list = prime_fibonacci()
print("List of prime Fibonacci series between 10 and 50 (using default arguments):",
      default_prime_fib_list)

# Using required arguments to generate a list of prime Fibonacci series between 20 and 100
required_prime_fib_list = prime_fibonacci(20, 100)
print("List of prime Fibonacci series between 20 and 100 (using required arguments):",
      required_prime_fib_list)

# Using keyword arguments to generate a list of prime Fibonacci series between 30 and 200
kwargs_prime_fib_list = prime_fibonacci(start=30, end=200)
print("List of prime Fibonacci series between 30 and 200 (using keyword arguments):",
      kwargs_prime_fib_list)
