# Data Validator with Error Handling - Create a system that validates data input and reports specific errors to the user.

# Function to validate user age input with error handling
def validate_age(age_str):
    try:
        age = int(age_str)  # Try converting input to integer
        if age < 0 or age > 120:
            return "Error: Age must be between 0 and 120."
        return f"Valid age: {age}"
    except ValueError:
        return "Error: Invalid input. Please enter a number."

# Simulate user input validation
print(validate_age("25"))     # Valid
print(validate_age("-5"))     # Invalid range
print(validate_age("abc"))    # Not a number

# Output:
# Valid age: 25
# Error: Age must be between 0 and 120.
# Error: Invalid input. Please enter a number.






# This function demonstrates best practices including:
# - Exception handling with try-except to manage type conversion errors (ValueError).
# - Input validation ensuring the integer falls within a realistic range (0 to 120).
# - Clear, explicit return messages indicating validation success or specific error causes.
# - Encapsulation of validation logic into a reusable function for modularity and testability.
# Note: Consider extending with logging or custom exceptions for enhanced error management.