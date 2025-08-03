# Example 1 – Creating a list and using append()

# Creates a list of fruits
fruits = ["apple", "banana"]

# Adds a new fruit to the list
fruits.append("orange")

print(fruits)  # Output: ['apple', 'banana', 'orange']




# Example 2 – Using remove()

# Removes 'banana' from the list
fruits.remove("banana")

print(fruits)  # Output: ['apple', 'orange']




# Example 3 – Using len()

# Counts how many items are in the list
print(len(fruits))  # Output: 2




# Example 4 – List slicing

# Creating a list of numbers
numbers = [10, 20, 30, 40, 50]
# From index 2 to the end
print(numbers[2:])         # Output: [30, 40, 50]
# From the start to index 1
print(numbers[:2])         # Output: [10, 20]
# From index 1 to 2
print(numbers[1:3])        # Output: [20, 30]
# From index 0 to 2, taking every 2nd element
print(numbers[0:3:2])      # Output: [10, 30]
# Full list (copy of the list)
print(numbers[:])          # Output: [10, 20, 30, 40, 50]
# Reversed list
print(numbers[::-1])       # Output: [50, 40, 30, 20, 10]

# List slicing uses the syntax: list[start:stop:step]
# - start: the index to start from (inclusive)
# - stop: the index to stop at (exclusive)
# - step: the interval between elements (default is 1)




# Example 5 – Creating a dictionary with key/value

# Creates a dictionary with person info
person = {
    "name": "Lucas",
    "age": 25,
    "city": "São Paulo"
}

print(person["name"])  # Output: Lucas
print(person["age"])   # Output: 25
print(person["city"])  # Output: São Paulo




# Example 6 – Adding a new key

# Adds a new key-value pair
person["email"] = "lucas@example.com"

print(person)
# Output: {'name': 'Lucas', 'age': 25, 'city': 'São Paulo', 'email': 'lucas@example.com'} 




# Example 7 – Using .keys(), .values() and .items()

# Prints all the keys in the 'person' dictionary
print(person.keys())    # Output: dict_keys(['name', 'age', 'city', 'email'])
# The dict_keys object behaves like an iterable containing all dictionary keys

# Prints all the values stored in the dictionary
print(person.values())  # Output: dict_values(['Lucas', 25, 'São Paulo', 'lucas@example.com'])
# Shows the values associated with each key, for example, 'Lucas' for the key 'name'

# Prints all key-value pairs (items) of the dictionary
print(person.items())   # Output: dict_items([('name', 'Lucas'), ('age', 25), ('city', 'São Paulo'), ('email', 'lucas@example.com')])
# Each item is a tuple (key, value), and the entire collection is an iterable of these tuples




# Example 8 – Checking if a key exists

# This line checks if the key "age" exists in the dictionary 'person'
if "age" in person:  # If the key "age" is found in 'person', this line will execute and print the message
    print("Age is present.")  # Output: Age is present.




# Example 9 – Removing a key with del

# The 'del' statement removes the key 'city' and its associated value from the 'person' dictionary
del person["city"]

# Now, when we print the dictionary, it no longer contains the 'city' key
print(person)
# Output: {'name': 'Lucas', 'age': 25, 'email': 'lucas@example.com'}

