# Practical Project with OOP

# Project 1 – Bank System: Conta, ContaCorrente, ContaPoupança

# Base class for common account behavior
class Account:
    def __init__(self, holder, balance=0):               # Constructor with default balance
        self.holder = holder                             # Account holder's name
        self.balance = balance                           # Account balance

    def deposit(self, amount):                           # Deposit method
        if amount > 0:                                   # Validating positive value
            self.balance += amount                       # Add to balance
            print(f"Deposit successful. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")             # Validation message

    def withdraw(self, amount):                          # Withdrawal method
        if amount > 0 and amount <= self.balance:        # Validate amount and balance
            self.balance -= amount                       # Subtract from balance
            print(f"Withdrawal successful. New balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")  # Error message

    def transfer(self, amount, target_account):          # Transfer to another account
        if amount > 0 and amount <= self.balance:        # Validation
            self.balance -= amount                       # Deduct from sender
            target_account.deposit(amount)               # Deposit to receiver
            print(f"Transferred {amount} to {target_account.holder}")
        else:
            print("Transfer failed due to invalid amount or insufficient funds.")

    def __str__(self):                                   # String representation
        return f"{self.holder} | Balance: {self.balance}"

# Subclass for Checking Account
class CheckingAccount(Account):
    def __init__(self, holder, balance=0, fee=5):        # Adds transaction fee
        super().__init__(holder, balance)                # Call base class constructor
        self.fee = fee                                   # Fee per withdrawal

    def withdraw(self, amount):                          # Override withdraw method
        total = amount + self.fee                        # Apply fee
        if total <= self.balance:                        # Check total with fee
            self.balance -= total                        # Subtract with fee
            print(f"Withdrawn {amount} + fee {self.fee}. New balance: {self.balance}")
        else:
            print("Insufficient funds for withdrawal + fee.")

# Subclass for Savings Account
class SavingsAccount(Account):
    def __init__(self, holder, balance=0, interest=0.02): # Adds interest attribute
        super().__init__(holder, balance)                # Call base class constructor
        self.interest = interest                         # Interest rate

    def apply_interest(self):                            # Method to apply interest
        earned = self.balance * self.interest            # Calculate interest
        self.balance += earned                           # Add to balance
        print(f"Interest of {earned} applied. New balance: {self.balance}")

# --- Test the system ---

# Create accounts
john = CheckingAccount("John", 100)                      # Checking account
alice = SavingsAccount("Alice", 200)                     # Savings account

# Operations
john.deposit(50)                                         # Deposit to John's account
john.withdraw(30)                                        # Withdraw from John's account  (with fee)
alice.apply_interest()                                   # Apply interest to Alice's account
john.transfer(50, alice)                                 # Transfer from John to Alice
print(john)                                              # Print John's account info
print(alice)                                             # Print Alice's account info

# Output:
# Deposit successful. New balance: 150
# Withdrawn 30 + fee 5. New balance: 115
# Interest of 4.0 applied. New balance: 204.0
# Deposit successful. New balance: 254.0
# Transferred 50 to Alice
# John | Balance: 65
# Alice | Balance: 254.0