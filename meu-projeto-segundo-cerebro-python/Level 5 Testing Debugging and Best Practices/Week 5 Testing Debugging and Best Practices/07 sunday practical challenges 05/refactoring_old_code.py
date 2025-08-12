# Refactoring Old Code - Take previously created code and apply refactoring, best practices, and comments.

# Old code - calculate area of rectangle, but repetitive
width1, height1 = 5, 10
area1 = width1 * height1
print("Area 1:", area1)

width2, height2 = 3, 7
area2 = width2 * height2
print("Area 2:", area2)

#Refactored code:
def calculate_area(width, height):
    """Calculate rectangle area."""
    return width * height

# Using the function to avoid repetition
print("Area 1:", calculate_area(5, 10))
print("Area 2:", calculate_area(3, 7))

# Output:
# Area 1: 50
# Area 2: 21






# Refactored code to improve maintainability and reduce redundancy.
# Key improvements:
# - Encapsulation of repeated logic (area calculation) inside a reusable function.
# - Clear function naming and docstring for better readability and documentation.
# - Function parameters make the code flexible for different inputs.
# - Reduces risk of errors and simplifies updates by centralizing the calculation logic.
# This approach follows the DRY principle (Don't Repeat Yourself).
