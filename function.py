# Q1: Write a function called greet() that prints "Hello, World!".

def greet():
    print("hello world")


greet()


# Q2: Write a function that takes a person's name as input and prints "Hello, <name>!". FUNCTION WITH ARGUMENT
def person(name):
    print(f"Hello , {name}! ")


person("Manasa")

# Q3: Write a function add_numbers(a, b) that returns the sum of two numbers.(func with return value)


def add_numbers(a, b):
    return a + b


result = add_numbers(5, 7)
print(result)


# Q4: Write a function power(base, exponent=2) that returns base raised to the power of exponent.
def power(base, exponent=2):
    return base ** exponent


print(power(5))
print(power(2, 3))

# Q5: Write a function average(numbers) that returns the average of all numbers in a list.


def average(numbers):
    if len(numbers) == 0:
        return 0  # or you could raise an error if you prefer
    return sum(numbers) / len(numbers)


# Example usage:
print(average([1, 2, 3, 4, 5]))  # Output: 3.0
print(average([]))                # Output: 0


# Q7: Write a recursive function factorial(n) that returns the factorial of n. Recursive function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(2))