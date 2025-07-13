# Example 1 – Variables and print()

# Creating simple variables with different data types
name = "Lucas"             # str (text)
age = 25                   # int (whole number)
height = 1.75              # float (decimal number)
has_license = True         # bool (true or false)

# Displaying the data on the screen
print("Name:", name)                # Output: Name: Lucas
print("Age:", age)                  # Output: Age: 25
print("Height:", height)            # Output: Height: 1.75
print("Has driver's license?", has_license)  # Output: Has driver's license? True




# Example 2 – Using type() to check variable types

# Checking the type of each variable
print(type(name))         # Output: <class 'str'>
print(type(age))          # Output: <class 'int'>
print(type(height))       # Output: <class 'float'>
print(type(has_license))  # Output: <class 'bool'>




# Example 3 – Using input() to get user input

# Let's assume the user enters: John and 30
name = input("Enter your name: ")   # User types: John
age = int(input("Enter your age: "))# User types: 30

print(f"{name} is {age} years old.")  # Output: John is 30 years old.




# Example 4 – Mini program combining everything

# Let's assume the user enters: Alice and 28
name = input("What is your name? ")    # User types: Alice
age = int(input("How old are you? "))  # User types: 28

birth_year = 2025 - age

print(f"{name}, you were born in {birth_year}.")  # Output: Alice, you were born in 1997.
