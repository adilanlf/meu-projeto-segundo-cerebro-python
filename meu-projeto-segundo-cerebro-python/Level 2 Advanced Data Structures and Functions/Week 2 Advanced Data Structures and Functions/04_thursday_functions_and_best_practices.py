# Default and Named Parameters

# Example 1 – Default parameter

# Defines a function with a default parameter
def greet(name="Guest"):
    print(f"Hello, {name}!") # Prints the greeting using f-string

greet("Lucas")    # Output: Hello, Lucas!
greet()           # Output: Hello, Guest!




# Example 2 – Named (keyword) arguments

# Default values for quantity and discount
def total_price(price, quantity=1, discount=0):
    total = price * quantity - discount   # Calculates total with discount
    print(f"Total: ${total:.2f}")         # Prints total formatted to 2 decimals

total_price(50, quantity=2, discount=10)  # Output: Total: $90.00
total_price(30)                           # Output: Total: $30.00




# **Flexible Functions with *args and kwargs

# Example 3 – *args for variable number of values

# *args collects all arguments as a tuple
def add_numbers(*args):
    print(f"Arguments received: {args}")    # Shows the received arguments
    total = sum(args)                       # Sums all values in args
    print(f"Sum: {total}")                  # Prints the result

add_numbers(1, 2, 3)        # Output: Sum: 6
add_numbers(10, 20, 30, 40) # Output: Sum: 100




# Example 4 – **kwargs for named dynamic arguments

# **kwargs collects named args as dict
def show_profile(**kwargs):
    for key, value in kwargs.items():             # Iterates through dictionary
        print(f"{key.capitalize()}: {value}")     # Prints key/value with capitalized key

show_profile(name="Ana", age=30, city="Berlin")
# Output:
# Name: Ana
# Age: 30
# City: Berlin




# Good Practices – Clean Code and Docstrings

# Example 5 – Docstring, clean naming and return

# Function to calculate the area of a rectangle
def calculate_area(width, height):
    """
    Calculates the area of a rectangle.

    Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Returns:
        float: The computed area.
    """
    return width * height  # area formula: width x height

# Call the function with values 5 and 3
area = calculate_area(5, 3)
print(f"Area: {area}")  # Output: Area: 15




# Summary (Quick Tips)

#  Use descriptive function and variable names
#  Use docstrings to explain purpose and usage
#  Default parameters help with flexibility
#  Use *args when you don’t know how many values will come
#  Use **kwargs when you expect dynamic named parameters