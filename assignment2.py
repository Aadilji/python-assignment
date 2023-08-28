# Question 1: Convert kilometers to miles
kilometers = float(input("Enter distance in kilometers: "))
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles:.2f} miles")

# Question 2: Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")

# Question 3: Display calendar
import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print("\n", calendar.month(year, month))

# Question 4: Solve quadratic equation
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Roots are real and different: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Root is real and equal: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print(f"Roots are complex: {real_part} + {imaginary_part}i, {real_part} - {imaginary_part}i")

# Question 5: Swap two variables without temp variable
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

print(f"Before swapping: x = {x}, y = {y}")
x, y = y, x 
print(f"After swapping: x = {x}, y = {y}")
