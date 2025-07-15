# Basic Dictionary: Key/Value Structure

# Example 1 – Creating and accessing values

# Creates a dictionary with personal data
person = {
    "name": "Lucas",
    "age": 25,
    "city": "São Paulo"
}

# Accessing values using keys
print(person["name"])  # Output: Lucas
print(person["age"])   # Output: 25
print(person["city"])  # Output: São Paulo




# Example 2 – Using .get() safely

# .get() avoids errors if the key doesn't exist
print(person.get("email"))  # Output: None (no error)
print(person.get("city"))   # Output: São Paulo
print(person.get("email", "Not provided"))  # Output: Not provided (default value if key doesn't exist)




# Example 3 – Looping with .items()

# .items() returns key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Lucas
# age: 25
# city: São Paulo




# Dictionary Operations: keys(), values(), in

# Example 4 – Getting keys and values

print(person.keys())    # Output: dict_keys(['name', 'age', 'city'])
print(person.values())  # Output: dict_values(['Lucas', 25, 'São Paulo'])
print(person.items())   # Output: dict_items([('name', 'Lucas'), ('age', 25), ('city', 'São Paulo')])




# Example 5 – Checking if a key exists

# Check if the key "age" exists in the 'person' dictionary
if "age" in person:
    # If the "age" key is present, print a confirmation message
    print(" 'age' is in the dictionary.")  # Output:  'age' is in the dictionary.

# Check if the key "email" does NOT exist in the 'person' dictionary
if "email" not in person:
    # If the "email" key is missing, print a warning message
    print(" 'email' is missing.")          # Output:  'email' is missing.





# Nested Dictionaries (Dictionary inside another)

# Example 6 – Creating and accessing nested data

# Dictionary of students with nested info
students = {
    "student1": {"name": "Anna", "grade": 9.0},
    "student2": {"name": "Bruno", "grade": 7.5}
}

# Accessing nested values
print(students["student1"]["name"])   # Output: Anna
print(students["student2"]["grade"])  # Output: 7.5




# Example 7 – Looping through nested dictionaries

# Loop through each student in the dictionary
for student_id, data in students.items():
    # Print student ID, name, and grade
    print(f"{student_id}: {data['name']} got {data['grade']}") # Prints the student ID, name, and grade using an f-string

# Example output:
# student1: Anna got 9.0
# student2: Bruno got 7.5

