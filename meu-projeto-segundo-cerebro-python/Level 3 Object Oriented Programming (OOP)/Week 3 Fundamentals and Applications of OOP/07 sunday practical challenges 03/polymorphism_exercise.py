# Polymorphism Exercise – Method Override

# Base class with a general method
class Animal:
    def speak(self):                # Default behavior
        return "Some sound"

# Dog overrides speak()
class Dog(Animal):
    def speak(self):
        return "Woof!"

# Cat overrides speak()
class Cat(Animal):
    def speak(self):
        return "Meow!"

# List of different animals
animals = [Dog(), Cat(), Animal()]   # Polymorphic list

# Loop through animals and call speak()
for animal in animals:
    print(animal.speak())            # Different result for each type
    
# Output:
# Woof!
# Meow!
# Some sound