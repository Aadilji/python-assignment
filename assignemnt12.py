# Question 1: Extract Unique Values from Dictionary Values
def extract_unique_values(dictionary):
    unique_values = set()
    for value_list in dictionary.values():
        unique_values.update(value_list)
    return list(unique_values)

my_dict = {'a': [1, 2, 3], 'b': [2, 3, 4], 'c': [4, 5, 6]}
unique_values = extract_unique_values(my_dict)
print("Unique values from dictionary values:", unique_values)

# Question 2: Find the Sum of All Items in a Dictionary
def sum_of_dict_items(dictionary):
    return sum(item for sublist in dictionary.values() for item in sublist)

sum_result = sum_of_dict_items(my_dict)
print("Sum of all items in the dictionary:", sum_result)

# Question 3: Merging two Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

# Question 4: Convert Key-Values List to Flat Dictionary
key_values_list = [('a', 1), ('b', 2), ('c', 3)]
flat_dict = dict(key_values_list)
print("Flat dictionary:", flat_dict)

# Question 5: Insertion at the Beginning in OrderedDict
from collections import OrderedDict

ordered_dict = OrderedDict([('a', 1), ('b', 2)])
ordered_dict.update({'c': 3})
ordered_dict.move_to_end('c', last=False)
print("OrderedDict after insertion at the beginning:", ordered_dict)

# Question 6: Check Order of Characters in String Using OrderedDict
def check_order_of_characters(string, pattern):
    pattern_dict = OrderedDict.fromkeys(pattern)
    j = 0
    for char in string:
        if char in pattern_dict:
            if char != pattern[j]:
                return False
            j += 1
            if j == len(pattern):
                break
    return True if j == len(pattern) else False

input_string = input("Enter a string: ")
pattern_string = input("Enter a pattern string: ")
if check_order_of_characters(input_string, pattern_string):
    print("The order of characters in the string matches the pattern")
else:
    print("The order of characters in the string does not match the pattern")

# Question 7: Sort Python Dictionaries by Key or Value
def sort_dict_by_key(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict

def sort_dict_by_value(dictionary):
    sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    return sorted_dict

my_dict = {'c': 3, 'a': 1, 'b': 2}
sorted_by_key = sort_dict_by_key(my_dict)
sorted_by_value = sort_dict_by_value(my_dict)
print("Dictionary sorted by key:", sorted_by_key)
print("Dictionary sorted by value:", sorted_by_value)
