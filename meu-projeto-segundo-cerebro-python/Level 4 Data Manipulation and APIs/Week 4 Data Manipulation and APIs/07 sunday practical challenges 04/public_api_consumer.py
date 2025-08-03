# Public API Consumer (show formatted data)

import requests

# Call a public API to get a random joke
response = requests.get("https://official-joke-api.appspot.com/random_joke")
data = response.json()                             # Parse JSON response

print(f"Joke: {data['setup']}")                    # Print joke setup
print(f"Answer: {data['punchline']}")              # Print punchline

#Output example:

#Joke: Did you hear about the guy who invented Lifesavers?
#Answer: They say he made a mint.






