# Inheritance and Code Reuse

# Example 1 – Basic Inheritance and Method Override

# Defining the parent class
class Animal:
    def __init__(self, name):                      # Constructor of the base class
        self.name = name                           # 'name' is a common attribute for all animals

    def speak(self):                               # Base method to be overridden
        print("This animal makes a sound.")        # Default message for any animal

# Defining the child class Dog, inheriting from Animal
class Dog(Animal):
    def speak(self):                               # Overriding the 'speak' method from Animal
        print(f"{self.name} says: Woof!")           # Specific message for dogs

# Another child class, Cat, also inherits from Animal
class Cat(Animal):
    def speak(self):                               # Overriding the 'speak' method for cats
        print(f"{self.name} says: Meow!")           # Specific message for cats

# Creating a Dog instance
d = Dog("Buddy")                                   # Object 'd' is a Dog with name "Buddy"

# Creating a Cat instance
c = Cat("Luna")                                    # Object 'c' is a Cat with name "Luna"

# Calling the overridden methods
d.speak()                                          # Prints → Buddy says: Woof!
c.speak()                                          # Prints → Luna says: Meow!

# Output:
# Buddy says: Woof!
# Luna says: Meow!




# Example 2 – Using super() in Child Class Constructor

# Defining the parent class Person
class Person:
    def __init__(self, name, age):                 # Constructor with two parameters
        self.name = name                           # Stores name
        self.age = age                             # Stores age

    def show_info(self):                           # Method to print basic info
        print(f"Name: {self.name}, Age: {self.age}")  # Displays name and age

# Defining the child class Employee
class Employee(Person):
    def __init__(self, name, age, job):            # Constructor with 3 parameters
        super().__init__(name, age)                # Calls the parent constructor (Person)
        self.job = job                             # Adds a new attribute 'job'

    def show_info(self):                           # Overrides method from Person
        super().show_info()                        # Calls the base method to show name and age
        print(f"Job: {self.job}")                  # Adds job info

# Creating an Employee instance
e = Employee("Maria", 28, "Engineer")              # Object 'e' with name, age and job

# Calling the overridden method
e.show_info()                                      # Prints full info (name, age, job)

# Output:
# Name: Maria, Age: 28
# Job: Engineer




# Example 3 – Inheriting Without Override

# Defining the base class
class Vehicle:
    def move(self):                                # Method available to all vehicles
        print("The vehicle is moving.")            # Default behavior

# Subclass that does not override anything
class Bike(Vehicle):                               # Bike inherits all behavior from Vehicle
    pass                                           # No new behavior defined here

# Creating a Bike instance
b = Bike()                                         # Object 'b' is an instance of Bike

# Calling inherited method
b.move()                                           # Prints the method from Vehicle class

# Output:
# The vehicle is moving.
# Note: The Bike class inherits the move method from Vehicle without overriding it.
# This demonstrates that inheritance allows reuse of existing methods without modification.
# The Bike class can use all methods defined in Vehicle as if they were its own.