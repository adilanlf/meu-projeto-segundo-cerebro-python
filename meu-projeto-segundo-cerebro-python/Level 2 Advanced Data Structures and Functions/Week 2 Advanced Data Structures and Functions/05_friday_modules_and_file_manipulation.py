# Modules in Python

# Example 1 – Importing a full module

import math                            # Imports the entire math module
print(math.sqrt(25))                   # Uses the sqrt() function √25 = 5.0
# Output: 5.0




# Example 2 – Importing only one function

from math import pi                    # Imports only the constant pi
print(pi)                              # Directly uses pi; value of π.
# Output: 3.141592653589793




# Example 3 – Using an alias

import datetime as dt                  # Imports the datetime module as "dt"
print(dt.datetime.now())               # Prints the current date and time
# Output: 2025-07-15 11:45:32.123456 (example)




# Example 4 – Creating and using a custom module

# Suppose you have a file named utils.py with the following contents:

# utils.py
def greet(name):                                 # Defines a greeting function
    return f"Hello, {name}!"                     # Returns the greeting message
# Now use this module in another file:
# main.py
#import utils                                     # Imports our custom utils module
#print(utils.greet("Lucas"))                      # Calls the greet function
# Output: Hello, Lucas!
# Note: Ensure that utils.py is in the same directory as main.py or in the Python path.




 # File Handling (.txt)

 # Example 5 – Writing to a text file

with open("example.txt", "w") as file:           # Opens the file in write mode ("w")
    file.write("Hello, world!\n")                # Writes the first line
    file.write("Second line.")                   # Writes the second line

# Content inside example.txt:
# Hello, world!
# Second line.
# Note: If example.txt already exists, it will be overwritten.
# If it doesn't exist, it will be created.





# Example 6 – Reading full content with .read()

with open("example.txt", "r") as file:           # Opens the file in read mode
    content = file.read()                        # Reads the entire file content
    print(content)                               # Prints all text as one string

# Output:
# Hello, world!
# Second line.
# Note: The content is read as a single string, including line breaks.




# Example 7 – Reading lines with .readlines()

with open("example.txt", "r") as file:           # Opens file for reading
    lines = file.readlines()                     # Reads all lines into a list
    print(lines)                                 # Prints the list of lines

# Output: ['Hello, world!\n', 'Second line.']
# Note: Each line is an element in the list, including line breaks.
# To access individual lines, you can use indexing:
# print(lines[0])  # Output: Hello, world!
# print(lines[1])  # Output: Second line.
# Note: To remove line breaks, you can use the strip() method:
# print(lines[0].strip())  # Output: Hello, world!
# print(lines[1].strip())  # Output: Second line.




# Example 8 – Appending content using "a" mode

with open("example.txt", "a") as file:           # Opens file in append mode
    file.write("\nThird line.")                  # Appends a new line at the end

# Final content inside example.txt:
# Hello, world!
# Second line.
# Third line.

# Note: The new line is added without overwriting existing content.
# If you read the file again, it will include the new line:
with open("example.txt", "r") as file:           # Opens file for reading
    content = file.read()                        # Reads the updated content
    print(content)                               # Prints all text including the new line
# Output:
# Hello, world!
# Second line.
# Third line.
# Note: Always ensure to close the file after operations, or use 'with' to handle it automatically.
# The 'with' statement automatically closes the file after the block is executed.   
# This prevents resource leaks and ensures the file is properly closed.
# If you need to close the file manually, you can use file.close() after the operations
# are done, but using 'with' is the recommended practice.




# Tips for Safe and Clean File Handling

#  Use 'with open()' to ensure files are properly closed
#  "w" = write (overwrites the file)
#  "a" = append (adds to existing content)
#  "r" = read
#  .read() returns everything as a single string
#  .readlines() returns a list of lines
