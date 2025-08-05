print("=== List Manipulation ===")
data = [5, 1, 9, 3, 7]

sorted_data = sorted(data)
print("Sorted list:", sorted_data)

even_numbers = [x for x in data if x % 2 == 0]
print("Even numbers:", even_numbers)

squared = [x**2 for x in data]
print("Squared numbers:", squared)

print("\n=== Tuple Manipulation ===")
my_tuple = (10, 20, 30)

print("Original tuple:", my_tuple)
print("First element:", my_tuple[0])


temp_list = list(my_tuple)
temp_list.append(40)
my_tuple = tuple(temp_list)

print("Modified tuple (after append):", my_tuple)

print("\n=== Find Second Largest ===")
def second_largest(numbers):
    unique_numbers = list(set(numbers))  
    if len(unique_numbers) < 2:
        return None  
    unique_numbers.sort(reverse=True)
    return unique_numbers[1]

nums = [4, 1, 7, 7, 3, 9, 9]
result = second_largest(nums)

if result is not None:
    print("Second largest number:", result)
else:
    print("List doesn't have enough unique numbers.")

print("\n=== Merge Dictionaries ===")
def merge_dicts(dict1, dict2):
    return dict1 | dict2  

dict_a = {'x': 1, 'y': 2}
dict_b = {'y': 3, 'z': 4}

merged = merge_dicts(dict_a, dict_b)
print("Merged dictionary:", merged)

