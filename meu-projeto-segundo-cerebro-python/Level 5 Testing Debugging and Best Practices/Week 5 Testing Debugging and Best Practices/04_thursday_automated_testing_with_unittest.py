# Automated Testing with unittest

# Example 1 – Basic test with unittest.TestCase

import unittest  # Import the unittest module to create and run tests

# Define a simple function that adds two numbers
def add(a, b):
    return a + b  # Return the sum of a and b

# Create a test case class by extending unittest.TestCase
class TestAddFunction(unittest.TestCase):

    def test_positive_numbers(self):
        # Check if the result of add(2, 3) is 5
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        # Check if the result of add(-2, -3) is -5
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        # Check if the result of add(0, 0) is 0
        self.assertEqual(add(0, 0), 0)

# This block allows the test to run when the file is executed directly
if __name__ == '__main__':
    unittest.main()  # Run all the test cases in the file


# Simulated Output:
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK




# Example 2 – Testing a reverse_string Function

import unittest  # Import the unittest module

# Define a function to reverse a string
def reverse_string(text):
    return text[::-1]  # Return the reversed string using slicing

# Define a test case class for reverse_string
class TestStringFunctions(unittest.TestCase):

    def test_normal_string(self):
        # Test if reversing "hello" returns "olleh"
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_empty_string(self):
        # Test if reversing an empty string returns an empty string
        self.assertEqual(reverse_string(""), "")

    def test_single_letter(self):
        # Test if reversing a one-letter string returns itself
        self.assertEqual(reverse_string("a"), "a")

# Run the test suite when the script is executed directly
if __name__ == '__main__':
    unittest.main()  # Run all defined test cases

# Simulated Output:
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.001s

# OK




# Example 3 – Showing a Failed Test

import unittest  # Import the unittest module

# Define a function to multiply two numbers
def multiply(x, y):
    return x * y  # Return the product of x and y

# Define a test case class for the multiply function
class TestMultiply(unittest.TestCase):

    def test_incorrect(self):
        # This test will fail because 2 * 3 = 6, not 5
        self.assertEqual(multiply(2, 3), 5)

# Run the test suite
if __name__ == '__main__':
    unittest.main()  # This will show a failure message

#Output:
# F
# ======================================================================
# FAIL: test_incorrect (__main__.TestMultiply.test_incorrect)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#  File "c:\Users\Negão\Desktop\segundo-cerebro-python\meu-projeto-segundo-cerebro-python\Level 5 Testing Debugging and Best Practices\a.py", line 14, in test_incorrect
#    self.assertEqual(multiply(2, 3), 5)
#AssertionError: 6 != 5
#
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
#
# FAILED (failures=1)




# Example 4 – Testing a Class with setUp() and tearDown()

import unittest  # Import the unittest module

# Sample class to test
class Calculator:

    # Add two numbers
    def add(self, x, y):
        return x + y

    # Multiply two numbers
    def multiply(self, x, y):
        return x * y

# Define a test case class for the Calculator
class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Runs before each test method
        self.calc = Calculator()  # Create a Calculator instance

    def tearDown(self):
        # Runs after each test method
        del self.calc  # Delete the Calculator instance

    def test_addition(self):
        # Check if add(4, 5) returns 9
        self.assertEqual(self.calc.add(4, 5), 9)

    def test_multiplication(self):
        # Check if multiply(3, 3) returns 9
        self.assertEqual(self.calc.multiply(3, 3), 9)

# Run the test cases when the script is executed
if __name__ == '__main__':
    unittest.main()

#Output:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK






# Summary: Why use unittest?
# Pros:
# Helps automate multiple tests.
# Clean structure for large projects.
# Identifies exact test failures.

# Ideal for:
# Functions with different edge cases.
# Projects where maintaining code stability is important.