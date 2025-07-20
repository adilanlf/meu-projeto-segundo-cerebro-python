# Vowel Counter in a Sentence

#This program:
#Prompts the user for a sentence
#Counts how many vowels (a, e, i, o, u) are in the sentence
#Ignores whether the sentence is uppercase or lowercase
#Uses for, lower(), if, in, and len()
#Includes comments and simulated output



# Gets a sentence from the user
sentence = input("Enter a sentence: ")  # e.g. "Python is Amazing!"

# Converts to lowercase for easier comparison
sentence = sentence.lower()

# Vowel list
vowels = "aeiou"
count = 0

# Loops through each character in the sentence
for letter in sentence:
    if letter in vowels:
        count += 1

print(f"Number of vowels: {count}")  # Output: Number of vowels: 5