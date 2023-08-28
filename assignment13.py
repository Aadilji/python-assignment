import math

# Question 1: Calculate and Print Values According to Formula
C = 50
H = 30

def calculate_q(D):
    return int(math.sqrt((2 * C * D) / H))

input_sequence = input("Enter comma-separated values of D: ")
D_values = [int(d) for d in input_sequence.split(',')]
result_values = [str(calculate_q(d)) for d in D_values]
print(','.join(result_values))

# Question 2: Generate a 2-Dimensional Array
X = int(input("Enter the number of rows (X): "))
Y = int(input("Enter the number of columns (Y): "))
array_2d = [[i * j for j in range(Y)] for i in range(X)]
print("Generated 2-dimensional array:")
for row in array_2d:
    print(row)

# Question 3: Sort Words Alphabetically
input_words = input("Enter comma-separated words: ")
sorted_words = sorted(input_words.split(','))
print(','.join(sorted_words))

# Question 4: Remove Duplicate Words and Sort Alphanumerically
input_words = input("Enter whitespace-separated words: ")
unique_words = sorted(set(input_words.split()))
print(' '.join(unique_words))

# Question 5: Count Letters and Digits in a Sentence
sentence = input("Enter a sentence: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
print(f"Number of letters: {letter_count}")
print(f"Number of digits: {digit_count}")

# Question 6: Check Password Validity
import re

def is_valid_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

password = input("Enter a password: ")
if is_valid_password(password):
    print("Valid password")
else:
    print("Invalid password")
