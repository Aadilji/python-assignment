# Question 1: Find the sum of elements in a list
def sum_of_elements(lst):
    return sum(lst)

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
sum_result = sum_of_elements(numbers)
print(f"The sum of elements in the list is {sum_result}")

# Question 2: Multiply all numbers in the list
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

product_result = multiply_list(numbers)
print(f"The product of all numbers in the list is {product_result}")

# Question 3: Find the smallest number in a list
smallest = min(numbers)
print(f"The smallest number in the list is {smallest}")

# Question 4: Find the largest number in a list
largest = max(numbers)
print(f"The largest number in the list is {largest}")

# Question 5: Find the second largest number in a list
sorted_numbers = sorted(numbers, reverse=True)
second_largest = sorted_numbers[1]
print(f"The second largest number in the list is {second_largest}")

# Question 6: Find N largest elements from a list
n_largest = int(input("Enter the value of N: "))
n_largest_elements = sorted_numbers[:n_largest]
print(f"The {n_largest} largest elements in the list are {n_largest_elements}")

# Question 7: Print even numbers in a list
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers in the list:", even_numbers)

# Question 8: Print odd numbers in a list
odd_numbers = [num for num in numbers if num % 2 != 0]
print("Odd numbers in the list:", odd_numbers)

# Question 9: Remove empty lists from a list
mixed_list = [1, [], 2, [], 3, [], [], 4]
non_empty_list = [item for item in mixed_list if item]
print("List with empty lists removed:", non_empty_list)

# Question 10: Cloning or Copying a list
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)

# Question 11: Count occurrences of an element in a list
element = int(input("Enter the element to count: "))
count = numbers.count(element)
print(f"The element {element} appears {count} times in the list")
