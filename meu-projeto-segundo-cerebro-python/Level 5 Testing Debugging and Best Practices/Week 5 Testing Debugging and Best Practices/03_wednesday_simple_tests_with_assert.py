# Simple Tests with assert - assert to check if functions are working correctly.

# Example 1 – Testing a function with assert

# Function to calculate the square of a number
def square(x):
    return x * x                             # Return x squared

# Assertions to test expected behavior
assert square(2) == 4                        # 2² = 4, should pass
assert square(0) == 0                        # 0² = 0, should pass
assert square(-3) == 9                       # (-3)² = 9, should pass

print("All tests passed!")                  # Show message if no assertion fails

# Output:
# All tests passed!




# Example 2 – Using assert to test inputs and outputs

# Function to reverse a word
def reverse_word(word):
    return word[::-1]                        # Return the word in reverse order

# Tests using assert
assert reverse_word("python") == "nohtyp"    # Reversed correctly
assert reverse_word("a") == "a"              # Single letter, no change
assert reverse_word("") == ""                # Empty string, still empty

print("String reversal tests passed!")

# Output:
# String reversal tests passed!




# Example 3 – When the test fails

# Function to add two numbers
def add(a, b):
    return a + b                             # Return the sum of a and b

# Intentional mistake in assert to simulate failure
assert add(2, 2) == 5                        # 2 + 2 = 4, not 5 → this will fail

print("Addition test passed!")              # This line will NOT run

# Output:
# AssertionError

# When assert fails, it stops the code and shows AssertionError.




# Example 4 – Testing function with custom messages

def multiply(a, b):
    return a * b                             # Return multiplication result

# Add custom error messages in case of failure
assert multiply(3, 4) == 12, "3 * 4 should be 12"
assert multiply(0, 10) == 0, "0 * 10 should be 0"
assert multiply(2, 5) == 10, "2 * 5 should be 10"

print("Multiplication tests passed!")

# Output:
# Multiplication tests passed!






# ✅ Best Practice Tip: Use assert
# - During function development.
# - To automate small logic tests.
# - In functions with predictable input (e.g., calculations, strings, lists).

# ❌ Avoid using assert:
# - For complex tests in production (use frameworks like unittest or pytest instead).
# - When you need detailed error messages and custom error handling.