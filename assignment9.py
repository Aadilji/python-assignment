# Question 1: Check if the given number is a Disarium Number
def is_disarium_number(n):
    num_str = str(n)
    power = 1
    sum_of_powers = sum(int(digit) ** power for power, digit in enumerate(num_str, start=1))
    return sum_of_powers == n

number = int(input("Enter a number: "))
if is_disarium_number(number):
    print(f"{number} is a Disarium number")
else:
    print(f"{number} is not a Disarium number")

# Question 2: Print all disarium numbers between 1 and 100
disarium_numbers = [num for num in range(1, 101) if is_disarium_number(num)]
print("Disarium numbers between 1 and 100:", disarium_numbers)

# Question 3: Check if the given number is a Happy Number
def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

number = int(input("Enter a number: "))
if is_happy_number(number):
    print(f"{number} is a Happy number")
else:
    print(f"{number} is not a Happy number")

# Question 4: Print all happy numbers between 1 and 100
happy_numbers = [num for num in range(1, 101) if is_happy_number(num)]
print("Happy numbers between 1 and 100:", happy_numbers)

# Question 5: Check if the given number is a Harshad Number
def is_harshad_number(n):
    return n % sum(int(digit) for digit in str(n)) == 0

number = int(input("Enter a number: "))
if is_harshad_number(number):
    print(f"{number} is a Harshad number")
else:
    print(f"{number} is not a Harshad number")

# Question 6: Print all pronic numbers between 1 and 100
def is_pronic_number(n):
    for i in range(1, n):
        if i * (i + 1) == n:
            return True
    return False

pronic_numbers = [num for num in range(1, 101) if is_pronic_number(num)]
print("Pronic numbers between 1 and 100:", pronic_numbers)
