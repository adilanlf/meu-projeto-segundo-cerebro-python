# Advanced Data Manipulation

# Example 1: Using the datetime module to manipulate dates and times

from datetime import datetime, timedelta  # Import datetime and timedelta classes

# Current date and time
now = datetime.now()                      # Get current date and time
print("Now:", now)                        # Print current datetime

# Formatting date as string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")  # Format datetime to string
print("Formatted:", formatted)                  # Output formatted date

# Adding 7 days to current date
week_later = now + timedelta(days=7)            # Calculate date 7 days ahead
print("Week later:", week_later.strftime("%Y-%m-%d"))

# Output (example):
# Now: 2025-08-01 15:40:01.061868
# Formatted: 2025-08-01 15:40:01
# Week later: 2025-08-08




# Example 2: Using collections.Counter to count occurrences

from collections import Counter  # Import Counter class

data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']  # List of fruits

counter = Counter(data)        # Count occurrences of each element
print(counter)                 # Print counts

# Most common element
most_common = counter.most_common(1)  # Get the most common item
print("Most common:", most_common)

# Output:
# Counter({'apple': 3, 'banana': 2, 'orange': 1
# Most common: [('apple', 3)]




# Example 3: Sorting lists and filtering data

products = [
    {"name": "Mouse", "price": 40},
    {"name": "Keyboard", "price": 100},
    {"name": "Monitor", "price": 600},
    {"name": "USB Cable", "price": 10}
]

# Sort products by price ascending
sorted_products = sorted(products, key=lambda p: p["price"])
print("Sorted by price:", sorted_products)

# Filter products with price > 50
expensive = list(filter(lambda p: p["price"] > 50, products))
print("Expensive products:", expensive)
# Output:
# Sorted by price: [{'name': 'USB Cable', 'price': 10}, {'name': 'Mouse', 'price': 40}, {'name': 'Keyboard', 'price': 100}, {'name': 'Monitor', 'price': 600}]
# Expensive products: [{'name': 'Keyboard', 'price': 100}, {'name': 'Monitor', 'price': 600}]




# Example 4: Data aggregation (sum and average)

prices = [p["price"] for p in products]   # Extract prices to a list

total = sum(prices)                        # Sum all prices
average = total / len(prices)              # Calculate average price

print(f"Total price: R${total}")
print(f"Average price: R${average:.2f}")
# Output:
# Total price: R$750
# Average price: R$187.50






# Summary (Key concepts)
# datetime.now() gets current date and time

# strftime() formats dates as strings

# timedelta adds or subtracts time periods

# collections.Counter counts frequency of items in iterable

# sorted() sorts lists by key or function

# filter() selects items based on condition

# sum() calculates total, length for average