# Example 1 – while loop

# Repeats while the number is less than 5
number = 0

while number < 5:
    print("Number:", number)
    number += 1

# Output:
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4




# Example 2 – for loop with range()

# Loops through numbers from 0 to 4 (5 is not included)
for i in range(5):
    print("i =", i)

# Output:
# i = 0
# i = 1
# i = 2
# i = 3
# i = 4




# Example 3 – for with custom range(start, stop, step)

# Loops from 10 to 0, decreasing by 2
for i in range(10, -1, -2):
    print(i)

# Output:
# 10
# 8
# 6
# 4
# 2
# 0




# Example 4 – Using break to stop the loop early

# Stops the loop when number equals 3
for i in range(10):
    if i == 3:
        break
    print("i =", i)

# Output:
# i = 0
# i = 1
# i = 2
# i = 3 (loop stops here, so this line is not printed)




# Example 5 – Using continue to skip an iteration

# Skips number 3, continues with the rest
for i in range(5):
    if i == 3:
        continue
    print("i =", i)

# Output:
# i = 0
# i = 1
# i = 2
# i = 4
# (number 3 is skipped, so it is not printed)




# Example 6 – while with break (user input simulation)

# Let's assume the user types: yes, yes, no
answer = ""
while True:
    answer = input("Do you want to continue? (yes/no): ")  # User types: yes → yes → no
    if answer == "no":
        break
    print("Continuing...")

# Output:
# Continuing...
# Continuing...
# (stops when user types "no")
# (no output for the last iteration since it breaks the loop)
