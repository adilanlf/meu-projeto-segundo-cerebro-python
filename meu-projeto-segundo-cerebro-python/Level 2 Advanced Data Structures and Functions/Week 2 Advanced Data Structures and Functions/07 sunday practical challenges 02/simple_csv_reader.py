# Simple CSV File Reader – Open a .csv file and display the formatted information.

def read_csv_file(filename):                    # Reads CSV file
    # This will fail if 'filename' does not exist or is not in the current directory
    with open(filename, "r") as file:           # Open file for reading
        lines = file.readlines()                 # Read all lines
    for line in lines:                           # Iterate through each line
        name, price = line.strip().split(",")    # Split line by comma into name and price
        print(f"{name} -> R${price}")            # Print formatted output

# Without error handling, this code will crash if:
# - The file does not exist (FileNotFoundError)
# - A line is empty or not properly formatted (ValueError)

# File 'products.csv' content:
# Mouse,50
# Keyboard,100
# Monitor,800

print(" Product List:")                          # Print header with emoji
read_csv_file("products.csv")                    # Call function with filename

# Output:
# Mouse -> R$50
# Keyboard -> R$100
# Monitor -> R$800




# Description:
# Reads and displays data from a CSV file (e.g., product name and price).
# Uses:
# - open() and readlines() to load file
# - .strip() to remove newline characters
# - .split(',') to convert CSV lines into lists
# - Loop to display each row