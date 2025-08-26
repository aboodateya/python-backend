# -------------------------------
# List Manipulation
# -------------------------------

print("=== List Manipulation ===")
data = [5, 1, 9, 3, 7]

# Sort list
sorted_data = sorted(data)
print("Sorted list:", sorted_data)

# Filter even numbers
even_numbers = [x for x in data if x % 2 == 0]
print("Even numbers:", even_numbers)

# Transform: square each number
squared = [x**2 for x in data]
print("Squared numbers:", squared)


# -------------------------------
# Tuple Manipulation
# -------------------------------

print("\n=== Tuple Manipulation ===")
my_tuple = (10, 20, 30)

# Accessing elements
print("Original tuple:", my_tuple)
print("First element:", my_tuple[0])

# Convert to list to modify
temp_list = list(my_tuple)
temp_list.append(40)
my_tuple = tuple(temp_list)

print("Modified tuple (after append):", my_tuple)


# -------------------------------
# Find Second Largest in List
# -------------------------------

print("\n=== Find Second Largest ===")
def second_largest(numbers):
    unique_numbers = list(set(numbers))  # Remove duplicates
    if len(unique_numbers) < 2:
        return None  # Not enough unique numbers
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

nums = [4, 1, 7, 7, 3, 9, 9]
result = second_largest(nums)

if result is not None:
    print("Second largest number:", result)
else:
    print("List doesn't have enough unique numbers.")


# -------------------------------
# Merge Dictionaries Using Union Operator
# -------------------------------

print("\n=== Merge Dictionaries ===")
def merge_dicts(dict1, dict2):
    return dict1 | dict2  # Requires Python 3.9+

dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 3, 'z': 4}

merged = merge_dicts(dict_a, dict_b)
print("Merged dictionary:", merged)


list_of_lists = [
    [10, 20, 4, 45, 99, 88],
    [5, 10, 15, 25, 40, 35, 60],
    [3, 2, 1],
    [100, 200, 300, 400, 500]
]
def second_largest(lst):
    if len(lst) < 2:
        return None 
    largest = second = float('-inf') 
    
    for num in lst:
        if num > largest:
            second = largest  
            largest = num     
        elif num > second and num != largest:
            second = num  
    return second

second_largest_list = [second_largest(sublist) for sublist in list_of_lists]

print("Second largest values in each list:", second_largest_list)
