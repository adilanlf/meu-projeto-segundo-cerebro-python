# Good Coding Practices

# PEP 8 – Python Enhancement Proposal 8
# PEP 8 is the official style guide for writing readable and standardized Python code.

#  Example following PEP 8
def calculate_average(grades):  # Function name uses lowercase with underscores
    total = sum(grades)         # Good variable name
    count = len(grades)
    return total / count        # Returns the average


#  Bad Example (Not PEP 8 compliant)
def CalculateAverage(GRADES):  # Wrong casing in function and variable names
    Total=0
    for G in GRADES:
        Total=Total+G
    return Total/len(GRADES)






#  Organizing Files and Folders

#my_project/
#│
#├── main.py            # Entry point
#├── utils.py           # Reusable functions
#├── data/              # Folder for .txt, .csv, etc.
#│   └── users.csv
#└── tests/             # Automated test scripts
#    └── test_main.py

#Why? Easy to maintain, scale, and find parts of the code.






# Naming Variables and Functions

# Good Examples
user_name = "John"        # Describes the data clearly
max_attempts = 5          # Lowercase with underscores (snake_case)
def get_user_input():     # Function name is action-based
    ...


# Bad Examples
x = "John"                # Too generic
A1 = 5                    # No meaning
def GU():                 # Not descriptive
    ...







# Useful vs Useless Comments

# Useful comment
def withdraw(self, amount):
    # Check if user has enough balance before withdrawing
    if amount <= self.balance:
        self.balance -= amount

# Useless comment
def withdraw(self, amount):
    # This function withdraws money
    if amount <= self.balance:  # If amount is less than balance
        self.balance -= amount  # Subtract amount from balance





# ----------------------------- 
#  Good Practices & Tips (Friday Recap)
# 
#     Follow PEP 8:
#   - Use snake_case for functions and variables
#   - Keep lines under 79 characters
#   - Use 4 spaces per indentation level
# 
#     Organize Your Project:
#   - Separate logic into modules (e.g., main.py, utils.py)
#   - Group data, scripts, and tests into dedicated folders
# 
#     Naming Matters:
#   - Choose clear, descriptive names (e.g., user_email, calculate_total)
#   - Avoid short or vague names (e.g., x, data1, func)
# 
#     Write Meaningful Comments:
#   - Comment WHY something is done (not WHAT is obvious)
#   - Avoid redundant or obvious comments
# 
#     Clean Code Tips:
#   - Keep functions short and focused
#   - Reuse code with helper functions
#   - Remove unused variables and code
# 
#     Result: Cleaner, readable, and maintainable Python code!
# -----------------------------

