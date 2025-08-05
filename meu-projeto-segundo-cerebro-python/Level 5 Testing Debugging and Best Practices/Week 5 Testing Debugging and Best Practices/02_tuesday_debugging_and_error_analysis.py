# Debugging and Error Analysis

# Example 1: Manual debugging with print()

def calculate_total(items):
    total = 0                                # Initialize total sum to zero
    for item in items:
        print(f"Item: {item}")               # Debug: show each item in the loop
        total += item                        # Add current item to total
    print(f"Total: {total}")                 # Debug: show the final total
    return total                             # Return the calculated total

items_list = [10, 20, 30]                    # Example list of numeric values
calculate_total(items_list)                  # Call the function with the list

# Output:
# Item: 10
# Item: 20
# Item: 30
# Total: 60




# Example 2: Using breakpoint() for Interactive Debugging

def greet(name):
    breakpoint()                             # Pause program and open debugger
    print(f"Hello, {name}!")                 # Print a greeting with the name

user_name = "Joyce"                         # Define a sample name
greet(user_name)                             # Call the greet function
#While paused at breakpoint(), you can inspect or change variables in the terminal. Try print(name) or type c to continue the execution.

#output:
# Hello, Joyce!




# Example 3: Understanding and Reading Tracebacks

def divide(a, b):
    return a / b                             # Risk of error if b = 0

def run_division():
    x = 10                                   # First number (numerator)
    y = 0                                    # Second number (denominator) – will cause error
    result = divide(x, y)                    # Call divide function – ZeroDivisionError expected
    print(result)                            # Print result if no error occurs

run_division()                               # Start the process

# Output:
# Traceback (most recent call last):
# File "main.py", line 52, in <module>
#    run_division()
# File "main.py", line 49, in run_division
#    result = divide(x, y)
# File "main.py", line 44, in divide
#    return a / b
#ZeroDivisionError: division by zero

# How to Read This Traceback:
# Last line – the exact error: ZeroDivisionError: division by zero
# Lines above – the path: which functions were called and on which lines
# Read it from bottom to top to understand the flow of the error






# Summary Table – Debugging Tools in Python

# Tool           Description
# print()        Displays the value of variables or expressions during runtime
#               (Most basic way to trace what's happening in your code)

# breakpoint()   Pauses the code and opens an interactive debug session
#               (Lets you inspect variables, step through code, and test changes live)

# Traceback      Shows where an error occurred and what type it was
#               (Automatically shown when an exception is raised; helps identify bugs)