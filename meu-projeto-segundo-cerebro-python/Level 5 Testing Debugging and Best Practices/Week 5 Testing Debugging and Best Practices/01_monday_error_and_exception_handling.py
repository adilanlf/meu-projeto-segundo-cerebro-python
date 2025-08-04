# Error and Exception Handling

# Example 1: Basic Try, Except to avoid errors

try:                                              # Start a block to attempt code that may cause an error
    num = int(input("Enter a number: "))          # Prompt user to enter a number and convert input to integer
    print(f"You entered: {num}")                   # Print the number that the user entered
except ValueError:                                 # Catch error if input cannot be converted to an integer
    print("Error: That's not a valid integer!")   # Print error message for invalid integer input


# Output if valid:
#Enter a number: 42
#You entered: 42

# Output if invalid:
#Enter a number: hello
#Error: That's not a valid integer!




# Example 2: Handling division by zero

try:                                             # Attempt risky code
    x = 10                                       # Set x to 10
    y = int(input("Enter a divisor: "))          # Get divisor from user
    result = x / y                               # Divide x by y
except ZeroDivisionError:                        # Handle division by zero error
    print("Error: Cannot divide by zero!")      # Show error message
else:                                            # If no error occurred
    print(f"Result: {result}")                   # Display the division result

# Output if valid divisor:
#Enter a divisor: 2
#Result: 5.0
# Output if zero divisor:
#Enter a divisor: 0
#Error: Cannot divide by zero!




# Example 3: Handling file not found error

try:                                             # Attempt to open and read a file
    with open("nonexistent_file.txt", "r") as file:  # Open file in read mode
        content = file.read()                    # Read the file content
except FileNotFoundError:                        # Handle case when file is missing
    print("Error: File not found!")              # Print error message
else:                                            # If file was read successfully
    print("File content:")                        # Print heading
    print(content)                                # Display the file content

# Output if file exists:
#File content:
#This is the content of the file.
# Output if file does not exist:
#Error: File not found!




# Example 4: Using finally for code that always executes

try:                                                    # Try to execute code that may raise an error
    num = int(input("Enter a positive number: "))       # Get user input and convert to integer
    if num < 0:
        raise ValueError("Number must be positive!")   # Raise error if number is negative
except ValueError as e:                                  # Catch ValueError and assign to variable e
    print(f"Error: {e}")                                # Print the error message
else:
    print(f"You entered {num}")                         # Print the valid input
finally:
    print("Execution finished.")                         # Always runs at the end

# Output if valid input:
#Enter a positive number: 5
#You entered 5
#Execution finished.
# Output if invalid input:
#Enter a positive number: -3
#Error: Number must be positive!
#Execution finished.
# Output if non-integer input:
#Enter a positive number: hello
#Error: invalid literal for int() with base 10: 'hello'
#Execution finished.






#Recap (Key concepts)
#Concept –    Description

#try     –     Block to test code that might raise errors

#except  –    Block that handles specified exceptions

#else    –    Runs if no exceptions occurred

#finally –   Runs always, even if exception occurs

#raise   –    Used to manually throw an exception
