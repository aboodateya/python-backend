# --- SETS ---

print("=== Sets: Creation, Operations, and Methods ===")
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
print("Original list:", nums)
print("Unique values using set:", unique_nums)

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric Difference:", a ^ b)

# Set methods
a.add(6)
print("After adding 6 to set a:", a)
a.discard(2)
print("After discarding 2 from set a:", a)

print("\n")


# --- DICTIONARIES ---

print("=== Dictionaries: Creation, Methods, and Comprehension ===")
# Dictionary creation
person = {'name': 'Alice', 'age': 25}
print("Person dictionary:", person)

# Methods
print("Keys:", person.keys())
print("Values:", person.values())
print("Get age:", person.get('age'))

# Update and pop
person.update({'city': 'New York'})
print("After update:", person)
person.pop('age')
print("After pop:", person)

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("Squares using comprehension:", squares)

print("\n")


# --- WALRUS OPERATOR ---

print("=== Walrus Operator Example ===")
# Classic loop
# while True:
#     val = input("Enter something (type 'quit' to stop): ")
#     if val == "quit":
#         break
#     print(val)

# Using Walrus
print("Type 'quit' to exit")
while (text := input("Enter something: ")) != "quit":
    print("You entered:", text)

print("\n")


# --- HANDS-ON: SET to remove duplicates ---

print("=== Remove Duplicates using Set ===")
items = ['apple', 'banana', 'apple', 'orange', 'banana']
unique_items = list(set(items))
print("Original:", items)
print("Without duplicates:", unique_items)

print("\n")


# --- HANDS-ON: Word frequency using dictionary ---

print("=== Word Frequency Counter ===")
sentence = "the quick brown fox jumps over the lazy dog the fox was quick"
words = sentence.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Word Frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")

print("\n")


# --- EXERCISE: Merge Dictionaries using Walrus Operator ---

print("=== Merge Two Dictionaries with Conflict Resolution (Walrus Operator) ===")
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}

merged = dict1.copy()

for key, value in dict2.items():
    if (existing := merged.get(key)) is not None:
        merged[key] = existing + value
    else:
        merged[key] = value

print("Merged Dictionary:", merged)
