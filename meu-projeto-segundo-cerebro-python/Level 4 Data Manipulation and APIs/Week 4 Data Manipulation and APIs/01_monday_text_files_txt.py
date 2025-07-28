# Text files (.txt)

# Example 1: Writing to a .txt file using with open()

# Open (or create) a file in write mode ("w")
with open("notes.txt", "w") as file:                     # Automatically closes the file after use
    file.write("First line of text.\n")                  # Write first line
    file.write("Second line of text.\n")                 # Write second line
    file.write("Learning file writing in Python.\n")     # Another line to practice

#Expected output (inside notes.txt file):
# First line of text.
# Second line of text.
# Learning file writing in Python.




# Example 2: Reading the whole file using read()

# Open the file in read mode
with open("notes.txt", "r") as file:       # Read mode to fetch file content
    content = file.read()                  # Read all content at once
    print(content)                         # Print the content

# Expected output on screen:
# First line of text.
# Second line of text.
# Learning file writing in Python.




# Example 3: Reading file line by line with a loop

# Open and read each line individually
with open("notes.txt", "r") as file:               # Using 'with' to auto-close file
    for i, line in enumerate(file):                # Loop through lines with index
        print(f"Line {i+1}: {line.strip()}")       # Show line number and strip newline

# Expected output:
# Line 1: First line of text.
# Line 2: Second line of text.
# Line 3: Learning file writing in Python.
# Note: The line numbers start from 1 for better readability.




# Example 4: Appending new content with "a" mode

# Append new lines to the existing file
with open("notes.txt", "a") as file:               # "a" appends without deleting content
    file.write("Fourth line added.\n")             # Add a new line
    file.write("Fifth line added.\n")              # Another new line

#New content in file after this:
# Fourth line added.
# Fifth line added.




# Summary (Key Concepts):
# open(filename, mode) – opens a file (modes: "r", "w", "a")

# .write() – writes text to file

# .read() – reads all text from file

# .strip() – removes whitespace and \n

# with open(...) as ...: – automatically manages closing the file

# "w" overwrites the file, "a" appends, "r" is for reading only