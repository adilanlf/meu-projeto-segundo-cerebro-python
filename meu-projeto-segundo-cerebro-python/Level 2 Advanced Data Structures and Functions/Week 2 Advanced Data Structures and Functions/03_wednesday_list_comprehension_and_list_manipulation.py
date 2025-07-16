# List Comprehension – Basic to Advanced

# Example 1 – Simple List Comprehension

# Creates a list with numbers from 0 to 4
numbers = [x for x in range(5)] # 'x for x in range(5)' means: for each number x from 0 to 4, include x in the list

print(numbers)  # Output: [0, 1, 2, 3, 4]




# Example 2 – List Comprehension with condition (if)

# Filters only even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]  # 'if x % 2 == 0' means: include x in the list only if it is divisible by 2 (i.e., even)

print(evens)  # Output: [0, 2, 4, 6, 8]




# Example 3 – List of squares

# Squares each number from 1 to 5
squares = [x**2 for x in range(1, 6)] # 'x**2' means: take the square of x (x multiplied by itself)

print(squares)  # Output: [1, 4, 9, 16, 25]




# Nested List Comprehension

# Example 4 – Flatten a matrix (2D list)

# Creates a list called 'matrix' that contains 3 sublists (nested lists)
# Each sublist represents a row in a 2D matrix (like a table or grid)
matrix = [[1, 2], [3, 4], [5, 6]]
# This line creates a new flat list called 'flat'
# It uses nested list comprehension to go through each sublist (row)
# and then through each element (num) in that row
flat = [num for row in matrix for num in row] # So: for each 'row' in 'matrix', for each 'num' in 'row', add 'num' to the new list

print(flat) # Prints the flattened list: [1, 2, 3, 4, 5, 6]



# Example 5 – Multiplication table using nested list comprehension

# Inner part: [x * y for y in range(1, 4)]
# - For each x, creates a list where y goes from 1 to 3
# - Multiplies x by y and adds the result to the row
# Creates a multiplication table (1 to 3)
table = [[x * y for y in range(1, 4)] for x in range(1, 4)] # Result: a multiplication table from 1 to 3

print(table)
# Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]




# Dynamic List Creation with Filter

# Example 6 – Filter strings starting with a specific letter

words = ["apple", "banana", "avocado", "grape", "apricot"] # Original list of words

# Creates a new list with only words that start with "a"
filtered = [word for word in words if word.startswith("a")]

print(filtered)  # Output: ['apple', 'avocado', 'apricot']




# Example 7 – Combine filtering and transformation

# Doubles even numbers from 1 to 10
result = [x * 2 for x in range(1, 11) if x % 2 == 0]

print(result)  # Output: [4, 8, 12, 16, 20]




# Example 8 – Remove spaces and convert to uppercase

names = [" lucas ", " ana", "BRUNO ", "marcos"]  # List with names having extra spaces and mixed cases

# Remove spaces at start/end and convert each name to uppercase
cleaned = [name.strip().upper() for name in names]

print(cleaned)  # Prints: ['LUCAS', 'ANA', 'BRUNO', 'MARCOS']