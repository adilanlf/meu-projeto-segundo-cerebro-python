# CPF Validator – receives a number and identifies whether it is valid (no regex).

# This code:
# Receives the CPF as user input
# Clears periods and dashes
# Checks for 11 numeric digits
# Validates the two CPF verification digits
# Without using re (regex)
# With comments and simulated output



def validate_cpf(cpf):
    # Remove spaces, dots and dashes
    cpf = cpf.replace(".", "").replace("-", "").strip()

    # Check if CPF has 11 digits and all are numbers
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Invalid CPFs with same digits repeated
    if cpf == cpf[0] * 11:
        return False

    # Calculates the first check digit
    sum1 = 0
    for i in range(9):
        sum1 += int(cpf[i]) * (10 - i)

    digit1 = (sum1 * 10) % 11
    if digit1 == 10:
        digit1 = 0

    # Calculates the second check digit
    sum2 = 0
    for i in range(10):
        sum2 += int(cpf[i]) * (11 - i)

    digit2 = (sum2 * 10) % 11
    if digit2 == 10:
        digit2 = 0

    # Compares calculated digits with the ones provided
    return cpf[-2:] == f"{digit1}{digit2}"

# === Main program ===

cpf_input = input("Enter your CPF (only numbers or formatted): ")  # User types: 529.982.247-25

if validate_cpf(cpf_input):
    print(" CPF is valid!")   # Output:  CPF is valid!
else:
    print(" CPF is invalid.") # Output:  CPF is invalid.
    