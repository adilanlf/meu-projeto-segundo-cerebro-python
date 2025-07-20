# Contacts List with File – Add, list, and search for contacts saved in .txt format.

def add_contact(name, phone):                           # Save contact to file
    with open("contacts.txt", "a") as file:             # Open file in append mode
        file.write(f"{name},{phone}\n")                 # Write contact line

def list_contacts():                                    # Read and list all contacts
    with open("contacts.txt", "r") as file:             # Open file in read mode
        for line in file:                               # Loop through each line
            name, phone = line.strip().split(",")       # Split line into name/phone
            print(f" {name}: {phone}")                  # Print contact formatted

add_contact("Alice", "1234-5678")                       # Add example contact
add_contact("Bob", "9876-4321")                         # Add another example

print("\nContact List:")                                # Print list title
list_contacts()                                         # Display all contacts

# Output:
#  Alice: 1234-5678
#  Bob: 9876-4321



# Description:
# Stores and manages contacts in a text file using CSV format (name,phone).
# Uses:
# - with open() for safe file operations
# - write() and read() methods
# - .split(',') to separate data fields
# - Functions to organize logic (add, list)