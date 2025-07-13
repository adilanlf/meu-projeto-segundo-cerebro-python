# Guessing Game (with limited attempts)

# Random number
# While loop with attempt limit
# Attack counter
# Hint messages (major/minor)
# Comments and mock exits



import random

# Generates a random number between 1 and 10
secret = random.randint(1, 10)

# Max number of attempts
max_attempts = 3
attempts = 0

print(" Guess the number between 1 and 10!")
print(f"You have {max_attempts} attempts.")

while attempts < max_attempts:
    guess = int(input("Your guess: "))  # Example: 5, 7, 10...
    attempts += 1

    if guess == secret:
        print(" Correct! You won!")   #  Output when the player guesses the correct number
        break  # Ends the game loop because the user guessed correctly
    elif guess < secret:
        print(" Too low.")  #  Output when the guess is lower than the secret number
    else:
        print(" Too high.")  #  Output when the guess is higher than the secret number

    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"You have {remaining} attempt(s) left.")  # ℹ Output showing how many attempts remain
    else:
        print(f" You lost! The number was {secret}.")  #  Output shown when the player runs out of attempts
