# TXT File Reader and Writer

# Open the file in write mode to store client data
with open("clients.txt", "w") as file:
    file.write("John Doe, johndoe@email.com\n")  # Write client info
    file.write("Jane Smith, janesmith@email.com\n")

# Open the file in read mode to retrieve data
with open("clients.txt", "r") as file:
    clients = file.read()                         # Read entire content

print("Clients stored:")
print(clients)                                   # Show clients list

# Output:

# Clients stored:
# John Doe, johndoe@email.com
# Jane Smith, janesmith@email.com