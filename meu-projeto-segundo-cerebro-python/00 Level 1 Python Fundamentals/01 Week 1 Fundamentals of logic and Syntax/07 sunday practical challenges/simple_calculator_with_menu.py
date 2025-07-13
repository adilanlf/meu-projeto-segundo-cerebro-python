# Challenge: Simple Calculator (with menu) – addition, subtraction, multiplication, division.

# Functions
# Conditional Structure
# Repetition (while)
# User Input
# Comments + Simulated Outputs



# Defines functions for each operation
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Menu loop
while True:
    print("\n=== Simple Calculator ===")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

    choice = input("Choose an option: ")  # Let's say user types: 1

    if choice == "0":
        print("Exiting the calculator. Goodbye!")
        break

    # Gets numbers from user
    num1 = float(input("Enter first number: "))  # e.g. 10
    num2 = float(input("Enter second number: ")) # e.g. 5

    # Performs the selected operation
    if choice == "1":
        result = add(num1, num2)
        print("Result:", result)        # Output: Result: 15.0
    elif choice == "2":
        result = subtract(num1, num2)
        print("Result:", result)
    elif choice == "3":
        result = multiply(num1, num2)
        print("Result:", result)
    elif choice == "4":
        result = divide(num1, num2)
        print("Result:", result)
    else:
        print("Invalid option. Try again.")
