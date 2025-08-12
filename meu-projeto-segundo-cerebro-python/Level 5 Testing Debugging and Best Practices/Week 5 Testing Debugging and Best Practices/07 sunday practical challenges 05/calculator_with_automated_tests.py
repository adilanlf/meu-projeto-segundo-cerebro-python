# Calculator with Automated Tests - Develop a calculator and apply tests with unittest.

import unittest

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(subtract(10, 7), 3)

if __name__ == '__main__':
    unittest.main()

# Output:
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s
# 
# OK





# Unit tests for basic calculator functions using Python's built-in unittest framework.
# Demonstrates:
# - Modular function design (add and subtract) for isolated testing.
# - Use of unittest.TestCase to organize test cases methodically.
# - Assertions (assertEqual) to verify expected output matches actual function results.
# - Standard test runner invocation with if __name__ == '__main__' guard to enable direct script execution.
# This setup ensures automated verification of functionality and simplifies future maintenance.
