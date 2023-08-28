# Question 1: Find the sum of an array
def array_sum(arr):
    return sum(arr)

array = [int(x) for x in input("Enter array elements separated by space: ").split()]
sum_result = array_sum(array)
print(f"The sum of the array elements is {sum_result}")

# Question 2: Find the largest element in an array
def find_largest_element(arr):
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest

largest = find_largest_element(array)
print(f"The largest element in the array is {largest}")

# Question 3: Array rotation
def rotate_array(arr, k):
    n = len(arr)
    k %= n  
    return arr[k:] + arr[:k]

k = int(input("Enter the number of rotations: "))
rotated_array = rotate_array(array, k)
print("Rotated array:", rotated_array)

# Question 4: Split the array and add the first part to the end
split_index = int(input("Enter the split index: "))
split_added_array = array[split_index:] + array[:split_index]
print("Array after split and addition:", split_added_array)

# Question 5: Check if given array is Monotonic
def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            increasing = False
        if arr[i] > arr[i - 1]:
            decreasing = False
    return increasing or decreasing

is_monotonic_result = is_monotonic(array)
if is_monotonic_result:
    print("The given array is monotonic")
else:
    print("The given array is not monotonic")
