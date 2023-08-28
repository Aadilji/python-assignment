import math

# Question 1: Find LCM
def lcm(x, y):
    return x * y // math.gcd(x, y)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
lcm_result = lcm(num1, num2)
print(f"LCM of {num1} and {num2} is {lcm_result}")

# Question 2: Find HCF
hcf_result = math.gcd(num1, num2)
print(f"HCF of {num1} and {num2} is {hcf_result}")

# Question 3: Convert Decimal to Binary, Octal, and Hexadecimal
decimal_num = int(input("Enter a decimal number: "))
binary_num = bin(decimal_num)[2:]
octal_num = oct(decimal_num)[2:]
hexadecimal_num = hex(decimal_num)[2:]
print(f"Binary: {binary_num}")
print(f"Octal: {octal_num}")
print(f"Hexadecimal: {hexadecimal_num}")

# Question 4: Find ASCII value of a character
char = input("Enter a character: ")
ascii_value = ord(char)
print(f"The ASCII value of '{char}' is {ascii_value}")

# Question 5: Simple Calculator with 4 basic mathematical operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice")
