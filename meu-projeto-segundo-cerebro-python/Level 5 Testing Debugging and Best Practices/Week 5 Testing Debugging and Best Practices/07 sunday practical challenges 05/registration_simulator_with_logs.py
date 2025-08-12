# User Registration Simulator with Exception Handling and Logging

import datetime

def log_error(message):
    with open("error_log.txt", "a") as file:
        timestamp = datetime.datetime.now()
        file.write(f"{timestamp} - ERROR: {message}\n")

def register_user(username, age_str):
    try:
        if len(username) < 3:
            raise ValueError("Username must be at least 3 characters long.")
        age = int(age_str)
        if age < 0:
            raise ValueError("Age cannot be negative.")
        print(f"User {username} registered successfully.")
    except ValueError as e:
        print(f"Registration failed: {e}")
        log_error(str(e))

# Simulate registrations
register_user("Al", "25")    # Username too short
register_user("Alice", "-2") # Negative age
register_user("Bob", "30")   # Success

#Output:
# Registration failed: Username must be at least 3 characters long.
# Registration failed: Age cannot be negative.
# User Bob registered successfully.






# User registration module with error handling and logging.
# Highlights:
# - Input validation for username length and age value with explicit ValueError raising.
# - Exception handling to catch validation errors and provide user feedback.
# - Centralized error logging to a file with timestamps for auditing and debugging.
# - Separation of concerns by isolating logging logic in a dedicated function.
# - Demonstrates robust handling of invalid inputs while maintaining program flow.