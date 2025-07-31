# Basic Web Scraping

# Example 1: Collect title from an HTML page

import requests                    # Library to make HTTP requests
from bs4 import BeautifulSoup     # Library to parse HTML content

# Step 1 – Request the web page
url = "https://example.com"                     # Simple test site
response = requests.get(url)                    # Make GET request

# Step 2 – Parse the HTML
soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML response

# Step 3 – Extract the title tag
title = soup.title.text                         # Get the text inside <title> tag
print("Page title:", title)

# Output (simulated):
# Page title: Example Domain





