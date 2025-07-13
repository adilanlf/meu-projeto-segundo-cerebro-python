# Example 1 – split()

# Splits a sentence into words
sentence = "Python is fun"

words = sentence.split()

print(words)  # Output: ['Python', 'is', 'fun']




# Example 2 – strip()

# Removes extra spaces from both ends of a string
raw_text = "   Hello world!   "

clean_text = raw_text.strip()

print(clean_text)  # Output: Hello world!




# Example 3 – f-string (formatted string)

# Inserts variables into a string using f-string
name = "Alice"
age = 30

print(f"{name} is {age} years old.")  # Output: Alice is 30 years old.




# Example 4 – .upper() and .lower()

text = "Python Rocks"

print(text.upper())  # Output: PYTHON ROCKS
print(text.lower())  # Output: python rocks




# Example 5 – .replace()

# Replaces part of a string with something else
message = "I like Java"

new_message = message.replace("Java", "Python")

print(new_message)  # Output: I like Python




# Example 6 – .find()

# Finds the position of a substring
text = "Welcome to Python"

position = text.find("Python")

print(position)  # Output: 11  (starts at index 11)




# Example 7 – Full combo

# Let's assume the user types:   lucas python
user_input = input("Enter your name and favorite language: ")  # User types:   lucas python

# Clean and split the input
cleaned = user_input.strip().split()

name = cleaned[0].capitalize()     # 'lucas' → 'Lucas'
language = cleaned[1].upper()      # 'python' → 'PYTHON'

print(f"{name} loves {language}!")  # Output: Lucas loves PYTHON!
