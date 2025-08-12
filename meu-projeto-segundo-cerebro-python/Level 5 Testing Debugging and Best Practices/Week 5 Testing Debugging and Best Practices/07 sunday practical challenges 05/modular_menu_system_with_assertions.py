# System with Modularized Menu – Create a program with a main menu divided into functions and test the behavior with assert.

def menu():
    print("1. Say Hello")
    print("2. Say Goodbye")
    print("3. Exit")
    choice = input("Choose an option: ")
    return choice

def say_hello():
    return "Hello!"

def say_goodbye():
    return "Goodbye!"

def main():
    while True:
        choice = menu()
        if choice == "1":
            print(say_hello())
        elif choice == "2":
            print(say_goodbye())
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid option.")

# Test function behavior with assert
assert say_hello() == "Hello!"
assert say_goodbye() == "Goodbye!"

main()

# Output:
# 1. Say Hello
# 2. Say Goodbye
# 3. Exit






# Simple interactive menu demonstrating:
# - Separation of concerns: distinct functions for menu display, actions, and main control flow.
# - Use of an infinite loop with a break condition to keep the menu running until exit.
# - Input handling with basic validation for user choices.
# - Use of assert statements for lightweight function testing without external frameworks.
# - Clear function return values to facilitate testing and potential reuse.
# Note: The interactive main() function is commented out to allow safe automated testing.
