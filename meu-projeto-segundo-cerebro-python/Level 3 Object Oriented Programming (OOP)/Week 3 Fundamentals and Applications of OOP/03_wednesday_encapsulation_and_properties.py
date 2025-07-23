# Encapsulation and Properties

# Example 1 – Encapsulation with _ and __

# Encapsulation is a fundamental principle of OOP that restricts direct access to an object's attributes and methods.

class BankAccount:                     # Defines a new class called BankAccount (represents a bank account)
    def __init__(self, owner, balance):  # Constructor method: initializes attributes when an object is created
        self.owner = owner              # Public attribute: accessible directly
        self._balance = balance         # Protected attribute (by convention, should not be accessed directly)
        self.__pin = "1234"             # Private attribute (name mangling used to prevent direct access)

# Create an instance
account = BankAccount("Alice", 1000)   # Instantiates a BankAccount object with owner "Alice" and balance 1000

print(account.owner)                   # Accessible: Alice (public attribute can be accessed directly)
print(account._balance)                # Possible but discouraged: 1000 (protected attribute by convention)
# print(account.__pin)                # Error: Attribute is private (raises AttributeError if accessed directly)

# Accessing the private attribute using name mangling
print(account._BankAccount__pin)       # Works, but not recommended: 1234 (bypasses privacy using name mangling)

# Output:
# Alice
# 1000
# 1234




# Example 2 – Getters and Setters with @property

class Product:                              # Defines a new class called Product (represents a product item)
    def __init__(self, name, price):        # Constructor method: initializes attributes when an object is created
        self.name = name                    # Public attribute: accessible directly
        self._price = price                 # "Private" attribute by convention (use underscore to indicate internal use)

    @property
    def price(self):                        # Getter method: allows read access to the _price attribute
        return self._price

    @price.setter
    def price(self, value):                 # Setter method: allows controlled write access to the _price attribute
        if value > 0:
            self._price = value             # Updates _price only if the new value is valid (positive)
        else:
            print("Invalid price!")         # Rejects invalid (non-positive) values

# Create a product
p = Product("Book", 50)                     # Creates a Product instance with name "Book" and price 50

print(p.price)                              # Calls the getter → Outputs: 50
p.price = 100                               # Calls the setter to update the price → Accepts new value
print(p.price)                              # Calls the getter again → Outputs: 100

p.price = -20                               # Calls the setter with an invalid value → Triggers error message

# Output:
# 50
# 100
# Invalid price!




# Example 3 – Controlling Access with Validation

class Student:                              # Defines a new class called Student (represents a student)
    def __init__(self, name):               # Constructor method: initializes attributes when an object is created
        self.name = name                    # Public attribute: can be accessed directly
        self._grades = []                   # Internal list for storing grades (treated as protected by convention)

    def add_grade(self, grade):             # Method to add a grade to the list
        if 0 <= grade <= 10:                # Validates that grade is within acceptable range (0–10)
            self._grades.append(grade)      # Adds grade to the internal list
        else:
            print("Grade must be between 0 and 10.")  # Rejects invalid grade

    @property
    def average(self):                      # Read-only property: calculates and returns the average grade
        if self._grades:                    # Checks if there are any grades to avoid division by zero
            return sum(self._grades) / len(self._grades)  # Returns average
        return 0                            # If no grades, average is 0

# Create student and add grades
s = Student("Lucas")                        # Creates a Student instance with name "Lucas"
s.add_grade(8)                              # Adds valid grade
s.add_grade(10)                             # Adds valid grade
s.add_grade(12)                             # Invalid grade → triggers validation message, not added

print(s.average)                            # Calls the average property → (8 + 10) / 2 = 9.0

# Output:
# Grade must be between 0 and 10.
# 9.0