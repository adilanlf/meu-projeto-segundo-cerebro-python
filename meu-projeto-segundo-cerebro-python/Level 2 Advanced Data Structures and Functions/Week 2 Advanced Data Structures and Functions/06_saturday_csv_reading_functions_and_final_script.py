# Reading and Writing CSV Files (using .split(','))

# Example 1 – Writing a simple CSV file

with open("products.csv", "w") as file:                     # Opens the CSV file for writing
    file.write("Name,Price\n")                              # Writes the header line
    file.write("Mouse,50\nKeyboard,120\nMonitor,800\n")     # Writes product data

# Content inside products.csv:
# Name,Price
# Mouse,50
# Keyboard,120
# Monitor,800
# Note: If products.csv already exists, it will be overwritten.
# If it doesn't exist, it will be created.




#  Example 2 – Reading the CSV file and splitting by comma

with open("products.csv", "r") as file:                     # Opens the CSV file for reading
    lines = file.readlines()                                # Reads all lines into a list

for line in lines:                                          # Loops through each line
    data = line.strip().split(",")                          # Removes newline and splits by comma
    print(data)                                             # Prints each row as a list

# Output:
# ['Name', 'Price']
# ['Mouse', '50']
# ['Keyboard', '120']
# ['Monitor', '800']
# Note: Each line is split into a list of values.
# To access individual values, you can use indexing:
# print(data[0])  # Output: Name (for the header)
# print(data[1])  # Output: Price (for the header)
# print(data[0])  # Output: Mouse (for the first product)
# print(data[1])  # Output: 50 (for the first product)
# Note: To convert the price to an integer, you can use int(data[1])
        



# Modularization – Reusable Functions

#  Example 3 – Defining functions to structure the code

def read_csv(filename):                         # Define function to read a CSV file
    with open(filename, "r") as file:           # Open the file in read mode
        lines = file.readlines()                # Read all lines from the file
    return [line.strip().split(",") for line in lines]  # Clean and split each line by comma

def display_products(data):                     # Define function to display products
    print("Product List:")                      # Print a title
    for row in data[1:]:                        # Loop through data, skipping header
        name, price = row                       # Unpack name and price
        print(f"- {name}: R${price}")           # Print formatted product info

def average_price(data):                        # Define function to calculate average price
    prices = [float(row[1]) for row in data[1:]] # Get prices as floats, skip header
    return sum(prices) / len(prices)            # Return the average of the prices




# Example 4 – Final Script – Uses Everything Learned

def main():                                                 # Main function to organize the script
    data = read_csv("products.csv")                         # Reads the CSV file
    display_products(data)                                  # Prints all products
    avg = average_price(data)                               # Calculates average
    print(f"\nAverage price: R${avg:.2f}")                  # Prints formatted average

main()                                                      # Calls the main function

# Output:
# Product List:
# - Mouse: R$50
# - Keyboard: R$120
# - Monitor: R$800
#
# Average price: R$323.33
# Note: Ensure that products.csv is in the same directory as this script or provide the correct path.
# This script reads a CSV file, displays the products, and calculates the average price.        
# It demonstrates how to structure code using functions for better organization and reusability.




# Good Practices Used

#  Clean code using functions (modular design)
#  Reuse logic for reading and processing CSV
#  Separation of concerns: read, process, display
#  Organized with a main() function for clarity
#  Easy to maintain and extend
