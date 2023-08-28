# Question 1: Find words greater than a given length k
def find_long_words(text, k):
    words = text.split()
    long_words = [word for word in words if len(word) > k]
    return long_words

input_text = input("Enter a sentence: ")
length_threshold = int(input("Enter the length threshold: "))
long_words = find_long_words(input_text, length_threshold)
print(f"Words longer than {length_threshold} characters: {long_words}")

# Question 2: Removing i-th character from a string
def remove_ith_char(text, i):
    return text[:i] + text[i+1:]

input_text = input("Enter a string: ")
i = int(input("Enter the index of the character to remove: "))
modified_text = remove_ith_char(input_text, i)
print("String after removing the i-th character:", modified_text)

# Question 3: Split and join a string
def split_and_join(text):
    words = text.split()
    return '-'.join(words)

input_text = input("Enter a string: ")
split_joined_text = split_and_join(input_text)
print("String after splitting and joining:", split_joined_text)

# Question 4: Check if a given string is a binary string
def is_binary_string(text):
    return all(char in '01' for char in text)

binary_text = input("Enter a string: ")
if is_binary_string(binary_text):
    print("The string is a binary string")
else:
    print("The string is not a binary string")

# Question 5: Find uncommon words from two strings
def find_uncommon_words(str1, str2):
    set1 = set(str1.split())
    set2 = set(str2.split())
    uncommon_words = (set1.symmetric_difference(set2))
    return uncommon_words

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
uncommon_words = find_uncommon_words(string1, string2)
print("Uncommon words between the two strings:", uncommon_words)

# Question 6: Find duplicate characters in a string
def find_duplicate_characters(text):
    duplicates = []
    for char in text:
        if text.count(char) > 1 and char not in duplicates:
            duplicates.append(char)
    return duplicates

input_text = input("Enter a string: ")
duplicate_chars = find_duplicate_characters(input_text)
print("Duplicate characters in the string:", duplicate_chars)

# Question 7: Check if a string contains any special character
import re

def has_special_character(text):
    pattern = re.compile('[!@#$%^&*(),.?":{}|<>]')
    return pattern.search(text) is not None

input_text = input("Enter a string: ")
if has_special_character(input_text):
    print("The string contains special characters")
else:
    print("The string does not contain special characters")
