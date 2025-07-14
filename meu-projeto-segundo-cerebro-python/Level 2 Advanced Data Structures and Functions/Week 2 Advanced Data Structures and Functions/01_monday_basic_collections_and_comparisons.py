# Tuples – Immutability and enumerate()

# Example 1 – Tuples are immutable

# Creates a tuple with 3 colors
colors = ("red", "green", "blue")

# Accessing the first element
print(colors[0])  # Output: red

# Tuples are immutable – the next line would cause an error if uncommented
# colors[0] = "yellow"  #  Error: 'tuple' object does not support item assignment





# Example 2 – Looping through a tuple with enumerate()

# Loop with index and value using enumerate
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# Output:
# 0: red
# 1: green
# 2: blue




# Sets – Removing duplicates, intersection, union

# Example 3 – Set automatically removes duplicates

# List with repeated names
names = ["Ana", "Ana", "Pedro", "Lucas", "Pedro"]

# Converts list to set (duplicates are removed)
unique_names = set(names)

print(unique_names)  # Output: {'Pedro', 'Lucas', 'Ana'}





# Example 4 – Set intersection (common elements)

# Two sets with some common elements
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Intersection: elements present in both sets
common = set1 & set2

print(common)  # Output: {3, 4}




# Example 5 – Set union (all unique elements)

# Union: all elements from both sets, without duplicates
union = set1 | set2

print(union)  # Output: {1, 2, 3, 4, 5, 6}





# Comparison: List vs Tuple vs Set

# Table Summary (commented in code)

# list: ordered, mutable, allows duplicates
# tuple: ordered, immutable, allows duplicates
# set: unordered, mutable, no duplicates

data = [1, 2, 2, 3]            # List with duplicates

as_tuple = tuple(data)        # Converts to tuple (same values)
as_set = set(data)            # Converts to set (removes duplicates)

print("List:", data)          # Output: List: [1, 2, 2, 3]
print("Tuple:", as_tuple)     # Output: Tuple: (1, 2, 2, 3)
print("Set:", as_set)         # Output: Set: {1, 2, 3}
