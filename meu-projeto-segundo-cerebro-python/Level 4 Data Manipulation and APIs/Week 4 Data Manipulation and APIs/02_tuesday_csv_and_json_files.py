# CSV and JSON files

# Part 1 –  .csv (comma-separated values) files

# Example 1: Writing CSV manually (with .join())

# Create data: list of lists
data = [
    ["Name", "Age", "City"],        # Header row
    ["Alice", "30", "New York"],    # First person
    ["Bob", "25", "São Paulo"],     # Second person
    ["Clara", "28", "Berlin"]       # Third person
]

# Open CSV file for writing
with open("people.csv", "w") as file:          # Open file in write mode
    for row in data:                           # Loop through each row
        file.write(",".join(row) + "\n")       # Join list by comma and add newline

#Result in people.csv:
#Name,Age,City
#Alice,30,New York
#Bob,25,São Paulo
#Clara,28,Berlin




# Example 2: Reading CSV manually with .split()

# Read CSV file manually
with open("people.csv", "r") as file:          # Open CSV file in read mode
    for line in file:                          # Read each line
        row = line.strip().split(",")          # Remove \n and split by comma
        print(row)                             # Print the row as list

#Output:
#['Name', 'Age', 'City']
#['Alice', '30', 'New York']
#['Bob', '25', 'São Paulo']
#['Clara', '28', 'Berlin']




# Example 3: Using csv module to read

import csv  # Import the csv module

# Read CSV using csv.reader
with open("people.csv", "r") as file:                  # Open CSV file
    reader = csv.reader(file)                          # Create CSV reader object
    for row in reader:                                 # Iterate through rows
        print(row)                                     # Print each row as list

#Output (same as above):
#['Name', 'Age', 'City']
#['Alice', '30', 'New York']
#['Bob', '25', 'São Paulo']
#['Clara', '28', 'Berlin']






# Parte 2 –  Arquivos .json (JavaScript Object Notation)

# Example 4: Saving data as JSON

import json  # Import the json module

# Dictionary with sample data
person = {
    "name": "Alice",                  # Name key
    "age": 30,                        # Age key
    "city": "New York",              # City key
    "skills": ["Python", "Excel"]    # List inside dict
}

# Save JSON to file
with open("person.json", "w") as file:      # Open file in write mode
    json.dump(person, file, indent=4)       # Dump dict to file with indentation

# person.json will look like:
# {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "skills": [
#         "Python",
#         "Excel"
#     ]
# }




# Example 5: Reading JSON from file

import json  # Import the json module

# Open and load JSON from file
with open("person.json", "r") as file:    # Open JSON file
    data = json.load(file)                # Load JSON into Python dictionary

print(data)                               # Print the dictionary
print(data["name"])                       # Access a specific value
# Output:
# {'name': 'Alice', 'age': 30, 'city': 'New York', 'skills': ['Python', 'Excel']}
# Alice






#Recap (Key Concepts)
# split(',') – breaks a CSV line into a list

# join(',') – joins list elements into CSV format

# csv.reader() – proper way to read CSV

# json.dump() – save dict to file

# json.load() – load dict from file

# JSON uses keys/values, CSV uses rows/columns