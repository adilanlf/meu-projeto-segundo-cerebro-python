# Working with REST APIs

# Example 1: Basic GET request using requests

import requests  # Import the requests library

# Make a GET request to a public API
response = requests.get("https://api.agify.io/?name=michael")  # Sends name as parameter in URL

# Convert the response JSON to a Python dictionary
data = response.json()  # Parses the JSON response

print(data)             # Print full dictionary
print(data['name'])     # Print name from response
print(data['age'])      # Print predicted age

#Output (simulated):
#{'count': 298219, 'name': 'michael', 'age': 64}
#michael
#64




# Example 2: Using parameters with params={}

import requests

# Base URL of the API
url = "https://api.agify.io/"

# Parameters for the request
params = {
    "name": "lucas",       # Name to predict age for
    "country_id": "BR"     # Optional country filter
}

# Send GET request with parameters
response = requests.get(url, params=params)

# Parse JSON response
data = response.json()

print(data)

#Output (simulated):
#{'count': 2123, 'name': 'lucas', 'age': 44, 'country_id': 'BR'}




# Example 3: Consuming Weather API (Open-Meteo)

import requests

# URL com latitude e longitude (São Paulo)
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -23.55,              # Latitude of São Paulo
    "longitude": -46.63,             # Longitude of São Paulo
    "current_weather": True          # Request current weather
}

# GET request with parameters
response = requests.get(url, params=params)

# Convert to JSON
weather = response.json()

# Extract current weather
print(weather["current_weather"])
#Output (simulated):
# {'time': '2025-07-30T19:00', 'interval': 900, 'temperature': 15.2, 'windspeed': 12.2, 'winddirection': 135, 'is_day': 1, 'weathercode': 1}




# Example 4: Simulated POST request

import requests

# URL de teste para POST
url = "https://httpbin.org/post"

# Dados a serem enviados
payload = {
    "username": "adilan",        # Simulated user input
    "password": "123456"
}

# Send POST request with JSON body
response = requests.post(url, json=payload)

# See what was sent and returned
print(response.json())

#Output (simulated):
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {},
#   "json": {
#     "username
#     "adilan
#     "password
#     "123456
#   },
#   "origin": "
#   "user-agent": "python-requests/2.25.1",
#   "url": "https://httpbin.org/post"
# }




# Example 5: Using Headers (e.g. authentication token)

import requests

# Fake API token
headers = {
    "Authorization": "Bearer ABC123XYZ"   # Token de autenticação (exemplo)
}

# Fake endpoint (httpbin testa headers)
response = requests.get("https://httpbin.org/headers", headers=headers)

# Check if token was sent
print(response.json())

#Output (simulated):
# {
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Authorization": "Bearer ABC123XYZ",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.31.0"  # Pode variar conforme a versão do requests
#   }
# }






# Concepts used in this code:
# requests.get(url)   -> Sends a GET request

# requests.post(url)  -> Sends data using a POST request

# .json()             -> Converts the response to a Python dictionary

# params={}           -> Sends URL query parameters

# headers={}          -> Sends request headers (e.g., access tokens)

# https://httpbin.org -> Test site used to simulate HTTP requests
