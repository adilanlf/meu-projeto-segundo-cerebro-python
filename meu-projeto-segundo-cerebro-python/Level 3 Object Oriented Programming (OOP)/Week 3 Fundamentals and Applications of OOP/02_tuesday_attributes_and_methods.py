# Attributes and Methods – Instance vs Class Attributes & Object Representation

# Example 1 – Instance Attributes vs Class Attributes

class Dog:
    species = "Canis familiaris"         # Class attribute (shared by all dogs)

    def __init__(self, name, age):       # Constructor method
        self.name = name                 # Instance attribute: unique name
        self.age = age                   # Instance attribute: unique age

# Creating instances of Dog
dog1 = Dog("Rex", 5)                     # dog1 has name "Rex" and age 5
dog2 = Dog("Luna", 3)                    # dog2 has name "Luna" and age 3

print(dog1.name)                         # Prints the name of dog1 → Rex
print(dog1.species)                      # Accessing class attribute → Canis familiaris
print(dog2.species)                      # Same class attribute for dog2

# Output:
# Rex
# Canis familiaris
# Canis familiaris




# Example 2 – Reading and Updating Attributes with Methods

class Dog:
    species = "Canis familiaris"         # Class attribute

    def __init__(self, name, age):       
        self.name = name                 # Instance attribute: name
        self.age = age                   # Instance attribute: age

    def bark(self):                      # Method that prints a bark
        print(f"{self.name} says woof!")

    def birthday(self):                  # Method that increases age by 1
        self.age += 1

    def get_age(self):                   # Returns the current age
        return self.age

# Create an object of Dog
dog = Dog("Max", 2)                      # Name: Max, Age: 2

dog.bark()                               # Calls bark() → Max says woof!
dog.birthday()                           # Increments age by 1 → Age becomes 3
print(dog.get_age())                     # Prints the updated age → 3

# Output:
# Max says woof!
# 3




# Example 3 – Using __str__() to Represent the Object

class Dog:
    species = "Canis familiaris"         # Class-level info

    def __init__(self, name, age):
        self.name = name                 # Stores name of the dog
        self.age = age                   # Stores age of the dog

    def __str__(self):                   # Custom string output when using print()
        return f"{self.name} is {self.age} years old."

# Creating a Dog object
dog = Dog("Buddy", 4)                    # Name: Buddy, Age: 4

print(dog)                               # Triggers __str__ method automatically

# Output:
# Buddy is 4 years old.