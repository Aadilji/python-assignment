# Question 1: Find the Factorial of a Number
number = int(input("Enter a number: "))
factorial = 1

if number < 0:
    print("Factorial is not defined for negative numbers")
elif number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, number + 1):
        factorial *= i
    print(f"Factorial of {number} is {factorial}")

# Question 2: Display the multiplication Table
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Question 3: Print the Fibonacci sequence
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

n = int(input("Enter the number of terms: "))
fib_sequence = fibonacci(n)
print("Fibonacci sequence:", fib_sequence)

# Question 4: Check Armstrong Number
number = int(input("Enter a number: "))
num_str = str(number)
num_digits = len(num_str)
sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)

if sum_of_digits == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

# Question 5: Find Armstrong Numbers in an Interval
lower = int(input("Enter the lower interval: "))
upper = int(input("Enter the upper interval: "))

print(f"Armstrong numbers between {lower} and {upper}:")
for num in range(lower, upper + 1):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    if sum_of_digits == num:
        print(num, end=" ")

# Question 6: Find the Sum of Natural Numbers
n = int(input("Enter a positive integer: "))
sum_natural = n * (n + 1) // 2
print(f"The sum of the first {n} natural numbers is {sum_natural}")
