# Refactoring and Code Cleanup

# Example 1: Refactoring Repeated Code into a Function

# -----------------------------
# Before: Repeated code (not efficient)

# Calculate the square of three different numbers
num1 = 4
num2 = 7
num3 = 10

# Square calculation (repeated logic)
print(f"The square of {num1} is {num1 ** 2}")
print(f"The square of {num2} is {num2 ** 2}")
print(f"The square of {num3} is {num3 ** 2}")

# Output (Before):
# The square of 4 is 16
# The square of 7 is 49
# The square of 10 is 100


# -----------------------------
# After: Refactored with a reusable function

# Define a function that calculates and prints the square of a number
def print_square(number):
    """Receives a number, calculates its square, and prints the result."""
    print(f"The square of {number} is {number ** 2}")

# Call the function for each number (no repeated code)
print_square(4)
print_square(7)
print_square(10)

#Output (After):
# The square of 4 is 16
# The square of 7 is 49
# The square of 10 is 100




# Example: Separating Responsibilities into Functions

# -----------------------------
# Function to get user input
def get_user_name():
    """Asks the user for their name and returns it."""
    return input("Enter your name: ")

# Function to greet the user
def greet_user(name):
    """Prints a welcome message for the user."""
    print(f"Hello, {name}! Welcome to the program.")

# Main program execution
username = get_user_name()  # Get the name from the user
greet_user(username)        # Greet the user with the provided name

# Example Output:
# Enter your name: Alice
# Hello, Alice! Welcome to the program.




# Example 3: Organizing into Multiple Files

#project/
#│
#├── main.py          # Main execution file
#├── math_utils.py    # Functions related to math
#└── greetings.py     # Functions related to greetings

# math_utils.py
def print_square(number):
    """Prints the square of a number."""
    print(f"The square of {number} is {number ** 2}")

#greetings.py
def greet_user(name):
    """Prints a greeting message."""
    print(f"Hello, {name}! Welcome to the program.")

#main.py
##from math_utils import print_square  # (commented code to avoid error, remove the comment to run)
##from greetings import greet_user # (commented code to avoid error, remove the comment to run)

# Use the imported functions
print_square(5)
greet_user("Bob")

# Output:
# The square of 5 is 25
# Hello, Bob! Welcome to the program.






# -----------------------------
#  Refactoring & Code Cleaning Tips:
# 
#     Avoid Code Duplication:
#   - Put repeated logic into reusable functions
# 
#     Single Responsibility Principle:
#   - Each function should have only ONE purpose
# 
#     Project Organization:
#   - Split code into multiple files (modules) based on functionality
# 
#     Keep it Clean:
#   - Remove unused variables, functions, and imports
# 
#     Easier Maintenance:
#   - Refactored code is easier to read, debug, and extend
# -----------------------------