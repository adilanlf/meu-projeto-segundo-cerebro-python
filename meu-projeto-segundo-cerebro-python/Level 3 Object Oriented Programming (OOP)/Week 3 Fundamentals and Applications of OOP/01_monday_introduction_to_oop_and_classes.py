# Introduction to OOP and Classes – Introduction to OOP (Object-Oriented Programming)

# Example 1 – Creating a Simple Class and Object

# Defining a class called 'Person'
class Person:
    def __init__(self, name, age):             # __init__ is a special method called when the object is created
        self.name = name                       # Instance attribute 'name'
        self.age = age                         # Instance attribute 'age'

    def greet(self):                           # Method that belongs to the class
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Creating an object (instance) of the Person class
p1 = Person("Alice", 30)                       # Object 'p1' is an instance of Person

p1.greet()                                     # Calls the method 'greet' of the object

# Output:
# Hello, my name is Alice and I'm 30 years old.




# Example 2 – Multiple Objects with Different Data

# Creating more instances with different data
p2 = Person("Bob", 25)
p3 = Person("Charlie", 40)

p2.greet()
p3.greet()

# Output:
# Hello, my name is Bob and I'm 25 years old.
# Hello, my name is Charlie and I'm 40 years old.




# Example 3 – Using Attributes Directly

print(p1.name)     # Accessing an attribute directly → Alice
print(p3.age)      # Accessing another attribute directly → 40

# Output:
# Alice
# 40