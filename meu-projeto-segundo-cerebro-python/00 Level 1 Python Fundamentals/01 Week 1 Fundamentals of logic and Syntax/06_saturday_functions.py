# Example 1 – Simple function without parameters

# Defines a function that prints a message
def greet():
    print("Hello!")

greet()  # Output: Hello!




# Example 2 – Function with parameters

# Defines a function that greets a person by name
def greet(name):
    print(f"Hello, {name}!")

greet("Lucas")  # Output: Hello, Lucas!




# Example 3 – Function with return

# Defines a function that adds two numbers and returns the result
def add(a, b):
    return a + b

result = add(5, 3)

print(result)  # Output: 8




# Example 4 – Function with default parameter

# If no name is given, use "Guest" by default
def greet(name="Guest"):
    print(f"Welcome, {name}!")

greet()         # Output: Welcome, Guest!
greet("Anna")   # Output: Welcome, Anna!




# SCOPE OF VARIABLES
# Example 5 – Local variables

def show_name():
    name = "Lucas"     # Local variable
    print(name)

show_name()            # Output: Lucas

# print(name)          # ❌ Error: name is not defined (outside the function)




# Example 6 – Global variable accessed within the function

name = "Anna"          # Global variable

def say_hello():
    print(f"Hello, {name}!")

say_hello()            # Output: Hello, Anna




# Example 7 – Modifying a global variable with global

counter = 0  # Global variable

def increment():
    global counter
    counter += 1

increment()
increment()

print(counter)  # Output: 2
