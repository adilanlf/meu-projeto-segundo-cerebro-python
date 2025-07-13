# Example 1 – if, elif, else

# Checks the temperature and prints a message accordingly
temperature = 30

if temperature > 35:
    print("It's very hot!")        # This line is not executed
elif temperature > 25:
    print("It's a warm day.")      # Output: It's a warm day.
else:
    print("It's a bit cold.")




# Example 2 – Another example with user input

# Let's assume the user types: 18
age = int(input("Enter your age: "))  # User types: 18

if age < 18:
    print("You are a minor.")           # This line is not executed
elif age == 18:
    print("You just became an adult!")  # Output: You just became an adult!
else:
    print("You are an adult.")




# Example 3 – Using Boolean in if

# Checks if the user is logged in
is_logged_in = True

if is_logged_in:
    print("Welcome back!")       # Output: Welcome back!
else:
    print("Please log in.")




# Example 4 – Ternary Operator (if in one line)

# Example of a one-line conditional (ternary operator)
age = 20
status = "Adult" if age >= 18 else "Minor"

print(status)   # Output: Adult




# Example 5 – Ternary with input()

# Let's assume the user types: Lucas
name = input("Enter your name: ")  # User types: Lucas

# Returns a greeting only if the name is not empty
greeting = f"Hello, {name}!" if name else "You didn't enter a name."

print(greeting)   # Output: Hello, Lucas!

