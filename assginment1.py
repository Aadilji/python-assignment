# Question 1: Print "Hello Python"
print("Hello Python")

# Question 2: Arithmetical operations (addition and division)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum_result = num1 + num2
division_result = num1 / num2
print("Sum:", sum_result)
print("Division:", division_result)

# Question 3: Calculate the area of a triangle
base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("Area of the triangle:", area)

# Question 4: Swap two variables
a = input("Enter the value of variable a: ")
b = input("Enter the value of variable b: ")
print("Before swapping: a =", a, "b =", b)
a, b = b, a  
print("After swapping: a =", a, "b =", b)

# Question 5: Generate a random number
import random
random_number = random.randint(1, 100)  
print("Random number:", random_number)
