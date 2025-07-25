# Polymorphism and Abstraction

# Example 1 – Polymorphism: Same Method Name in Different Classes

class Bird:
    def speak(self):                          # Method defined in base-like class
        print("Some generic bird sound")      # Default behavior

class Parrot:
    def speak(self):                          # Same method name as Bird
        print("Parrot says: Hello!")          # Specific behavior for Parrot

class Duck:
    def speak(self):                          # Same method name as others
        print("Duck says: Quack!")            # Specific behavior for Duck

# Function that uses polymorphism
def make_it_speak(animal):                    # Accepts any object with 'speak' method
    animal.speak()                            # Calls the appropriate version based on the object

# Creating instances
b = Bird()                                    # Object from Bird class
p = Parrot()                                  # Object from Parrot class
d = Duck()                                    # Object from Duck class

# Using the same function with different objects
make_it_speak(b)                              # Output → Some generic bird sound
make_it_speak(p)                              # Output → Parrot says: Hello!
make_it_speak(d)                              # Output → Duck says: Quack!




# Example 2 – Abstract Class Using abc Module

from abc import ABC, abstractmethod            # Importing tools to create abstract classes

# Defining an abstract base class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):                     # Abstract method (must be implemented)
        pass                                  # No body here, just definition

# Subclass implementing the abstract method
class Dog(Animal):
    def make_sound(self):                     # Implements make_sound
        print("Dog barks: Woof!")             # Specific behavior

# Another subclass implementing the method
class Cat(Animal):
    def make_sound(self):                     # Implements make_sound
        print("Cat meows: Meow!")             # Specific behavior

# Creating instances of the subclasses
dog = Dog()
cat = Cat()

# Calling the implemented methods
dog.make_sound()                              # Output → Dog barks: Woof!
cat.make_sound()                              # Output → Cat meows: Meow!

# Note: You can't create an instance of Animal directly because it's abstract




# Example 3 – Simple Class Hierarchy with Polymorphism

class Employee:
    def calculate_salary(self):               # Base method for salary calculation
        return 0                              # Default behavior

class Manager(Employee):
    def calculate_salary(self):               # Override for Manager
        return 5000                           # Manager earns fixed amount

class Developer(Employee):
    def calculate_salary(self):               # Override for Developer
        return 4000 + 500                     # Developer gets bonus

# List of employees (polymorphic objects)
staff = [Manager(), Developer(), Developer()]

# Loop to calculate total payroll
total = 0
for person in staff:                          # Loop through each employee
    total += person.calculate_salary()        # Calls the appropriate method based on class

print(f"Total payroll: ${total}")             # Output → Total payroll: $14000