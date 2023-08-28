import math

# Question 1: Display Fibonacci Sequence Using Recursion
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(n)
print("Fibonacci sequence:", fib_sequence)

# Question 2: Find Factorial of Number Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")

# Question 3: Calculate Body Mass Index (BMI)
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")

# Question 4: Calculate Natural Logarithm of a Number
number = float(input("Enter a number: "))
natural_log = math.log(number)
print(f"The natural logarithm of {number} is {natural_log:.2f}")

# Question 5: Cube Sum of First n Natural Numbers
def cube_sum(n):
    return (n * (n + 1) // 2) ** 2

n = int(input("Enter a positive integer: "))
result = cube_sum(n)
print(f"The cube sum of the first {n} natural numbers is {result}")
