# Random Password Generator – Generate passwords with letters, numbers, and symbols using random code.

import random
import string

def generate_password(length=10):                       # Default password length is 10
    chars = string.ascii_letters + string.digits + string.punctuation  # Letters, digits, symbols
    password = ''.join(random.choice(chars) for _ in range(length))   # Pick random characters
    return password

print(" Your password:", generate_password(12))       # Generate and print password

# Example output:
#  Your password: w2R!e9#Kb@Lq




# Description:
# Generates secure passwords using letters, digits, and symbols.
# Uses:
# - random module for randomness
# - string module to access character sets
# - ''.join() to build the final password string
# - Function with default parameter (length=10)