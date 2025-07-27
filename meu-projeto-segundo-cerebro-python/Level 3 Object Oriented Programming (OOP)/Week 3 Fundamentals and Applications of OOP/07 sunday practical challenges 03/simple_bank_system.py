# Simple Bank System – No Negative Balance

# A class that models a simple bank account
class SimpleAccount:
    def __init__(self, owner, balance=0):    # Constructor
        self.owner = owner                  # Account owner's name
        self.balance = balance              # Initial balance

    def deposit(self, amount):              # Method to deposit money
        if amount > 0:                      # Must be a positive amount
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):             # Method to withdraw money
        if 0 < amount <= self.balance:      # Only if enough balance
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Withdrawal failed: insufficient funds.")

# Test account
acc = SimpleAccount("Maria", 100)
acc.deposit(50)        # Deposit 50
acc.withdraw(30)       # Withdraw 30
acc.withdraw(150)      # Try to overdraw

# Output:
# 50 deposited. New balance: 150
# 30 withdrawn. New balance: 120
# Withdrawal failed: insufficient funds