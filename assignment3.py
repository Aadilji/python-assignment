# Question 1: Check if a number is Positive, Negative, or Zero
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Question 2: Check if a number is Odd or Even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Question 3: Check Leap Year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Question 4: Check Prime Number
number = int(input("Enter a number: "))
is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

# Question 5: Print all Prime Numbers in an Interval of 1-10000
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

print("Prime numbers between 1 and 10000:")
for num in range(1, 10001):
    if is_prime(num):
        print(num, end=" ")
