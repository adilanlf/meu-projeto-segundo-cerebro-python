# Rock, Paper, Scissors Game – User interaction and victory through simple rules.

import random                                          # Import random module

options = ["rock", "paper", "scissors"]                # Define possible choices
user = input("Choose rock, paper or scissors: ").lower()  # Get user input, convert to lowercase
bot = random.choice(options)                           # Randomly select bot choice

print(f"You chose: {user}")                            # Display user choice
print(f"Bot chose: {bot}")                             # Display bot choice

# Determine winner
if user == bot:                                        # Check for tie
    print(" It's a tie!")                           
elif (user == "rock" and bot == "scissors") or \
     (user == "scissors" and bot == "paper") or \
     (user == "paper" and bot == "rock"):
    print(" You win!")
else:                                                  # Otherwise, user loses
    print(" You lose!")

# Example output:
# You chose: rock
# Bot chose: scissors
# You win!




# Description:
# Interactive game between user and computer with win/loss logic.
# Uses:
# - input() to get player choice
# - random.choice() for computer move
# - if/elif/else to compare choices and determine winner
# - Emoji and formatted messages for better UX