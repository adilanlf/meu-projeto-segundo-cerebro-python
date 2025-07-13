# Product Registration with List Menu
    
#Allows you to:
#Add product (with name and price)
#Remove product by name
#List all products
#Calculate average prices
#All with lists, dictionaries, while, if, input(), and f-strings
#Comments and output included 



# Empty list to store products
products = []

while True:
    print("\n=== PRODUCT MENU ===")
    print("1 - Add product")
    print("2 - Remove product")
    print("3 - List products")
    print("4 - Average price")
    print("0 - Exit")

    option = input("Choose an option: ")  # Let's say: 1

    if option == "0":
        print("Exiting program. Bye!")
        break

    elif option == "1":
        name = input("Product name: ")           # e.g. Banana
        price = float(input("Product price: "))  # e.g. 2.50

        # Adds a dict to the list
        products.append({"name": name, "price": price})
        print(f"{name} added successfully.")      # Output: Banana added successfully.

    elif option == "2":
        name = input("Product name to remove: ")  # e.g. Banana
        found = False

        for product in products:
            if product["name"].lower() == name.lower():
                products.remove(product)
                print(f"{name} removed.")         # Output: Banana removed.
                found = True
                break

        if not found:
            print("Product not found.")

    elif option == "3":
        if not products:
            print("No products registered.")
        else:
            print("\n--- Product List ---")
            for product in products:
                print(f"{product['name']} - R${product['price']:.2f}")
            # Output example:
            # Banana - R$2.50
            # Apple - R$3.00

    elif option == "4":
        if not products:
            print("No products to calculate average.")
        else:
            total = sum(p["price"] for p in products)
            avg = total / len(products)
            print(f"Average price: R${avg:.2f}")   # Output: Average price: R$2.75

    else:
        print("Invalid option. Try again.")  # Output: Invalid option. Try again.
