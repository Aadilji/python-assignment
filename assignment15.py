# Question 1: Class with a Generator for Divisible Numbers
class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def divisible_by_seven_generator(self):
        for num in range(self.n + 1):
            if num % 7 == 0:
                yield num

n = int(input("Enter a value for n: "))
divisible_by_seven = DivisibleBySeven(n)
gen = divisible_by_seven.divisible_by_seven_generator()
print(f"Divisible by 7 between 0 and {n}:")
for num in gen:
    print(num, end=' ')

# Question 2: Compute Frequency of Words and Sort Keys
input_text = input("Enter a sentence: ")
word_frequency = {}
for word in input_text.split():
    word_frequency[word] = word_frequency.get(word, 0) + 1
sorted_word_frequency = dict(sorted(word_frequency.items()))
print("Frequency of words:", sorted_word_frequency)

# Question 3: Define Classes and Inheritance
class Person:
    def get_gender(self):
        return "Unknown"

class Male(Person):
    def get_gender(self):
        return "Male"

class Female(Person):
    def get_gender(self):
        return "Female"

person1 = Male()
person2 = Female()
print("Person 1:", person1.get_gender())
print("Person 2:", person2.get_gender())

# Question 4: Generate Sentences with Given Conditions
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]

sentences = [(subject, verb, obj) for subject in subjects for verb in verbs for obj in objects]
for subject, verb, obj in sentences:
    print(f"{subject} {verb} {obj}")

# Question 5: Compress and Decompress String
import zlib

original_string = "hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(original_string.encode())
decompressed_string = zlib.decompress(compressed_string).decode()
print("Original string:", original_string)
print("Compressed string:", compressed_string)
print("Decompressed string:", decompressed_string)

# Question 6: Binary Search Function
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
search_item = int(input("Enter the item to search: "))
index = binary_search(sorted_list, search_item)
if index != -1:
    print(f"Item {search_item} found at index {index}")
else:
    print(f"Item {search_item} not found in the list")
