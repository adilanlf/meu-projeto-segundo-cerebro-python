# Basic Web Scraping
#two ## in the code to avoid errors, just import the library and remove the two ## parts

# Example 1: Collect title from an HTML page

import requests                    # Library to make HTTP requests
##from bs4 import BeautifulSoup     # Library to parse HTML content  # (uncomment if you want to use BeautifulSoup)

# Step 1 – Request the web page
url = "https://example.com"                     # Simple test site
response = requests.get(url)                    # Make GET request

# Step 2 – Parse the HTML
##soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML response # (uncomment if you want to use BeautifulSoup)

# Step 3 – Extract the title tag
##title = soup.title.text                         # Get the text inside <title> tag # (uncomment if you want to use BeautifulSoup)
##print("Page title:", title)   # Print the page title # (uncomment if you want to use BeautifulSoup)

# Output (simulated):
# Page title: Example Domain




# Example 2: Collect all links from a page

import requests                                 # Import the 'requests' library to make HTTP requests
##from bs4 import BeautifulSoup                   # Import 'BeautifulSoup' from 'bs4' to parse HTML content # (uncomment if you want to use BeautifulSoup)

url = "https://example.com"                     # Define the URL to send the HTTP request to
response = requests.get(url)                    # Send a GET request to the URL and store the response
##soup = BeautifulSoup(response.text, "html.parser")  # Parse the HTML content of the response using BeautifulSoup # (uncomment if you want to use BeautifulSoup)

# Find all <a> tags (hyperlinks)
##links = soup.find_all('a')                      # Find and store all anchor tags (<a>) from the HTML # (uncomment if you want to use BeautifulSoup)

# Loop to print all link hrefs
##for link in links:                              # Iterate through each anchor tag # (uncomment if you want to use BeautifulSoup)
##    print(link['href'])                         # Print the value of the 'href' attribute (the URL) # (uncomment if you want to use BeautifulSoup)

# Output (simulated)
# https://www.iana.org/domains/example




# Exemplo 3: Scraping com filtros (classes e tags)
#Let's simulate a page with multiple <p> and a <div class="info">.

html = """
<html>
  <body>
    <div class="info">Python Web Scraping Guide</div>
    <p>Learn how to scrape with Python</p>
    <p class="highlight">Important content</p>
  </body>
</html>
"""

##from bs4 import BeautifulSoup # (uncomment if you want to use BeautifulSoup)

# Parse the raw HTML string
##soup = BeautifulSoup(html, "html.parser") # (uncomment if you want to use BeautifulSoup)

# Get the div with class "info"
##info = soup.find("div", class_="info").text     # Find a specific div by class # (uncomment if you want to use BeautifulSoup)
##print("Info:", info)  # (uncomment if you want to use BeautifulSoup)

# Get all paragraphs
##paragraphs = soup.find_all("p")                 # Find all <p> tags # (uncomment if you want to use BeautifulSoup)
##for p in paragraphs: # (uncomment if you want to use BeautifulSoup)
##    print("Paragraph:", p.text)                 # Print paragraph text # (uncomment if you want to use BeautifulSoup)

# Output (simulated):
# Info: Python Web Scraping Guide   
# Paragraph: Learn how to scrape with Python
# Paragraph: Important content




# Example 4: Saving data to a .txt file

# Let's say we already scraped some data
scraped_data = ["Python", "BeautifulSoup", "Scraping", "HTML"]   # Sample list of scraped data strings

# Save to a file
with open("scraped_data.txt", "w", encoding="utf-8") as file:    # Open a text file in write mode with UTF-8 encoding
    for item in scraped_data:                                    # Loop through each item in the scraped data list
        file.write(item + "\n")                                   # Write each item followed by a newline character

print("Data saved to scraped_data.txt")                          # Print confirmation message after saving

# File output (scraped_data.txt):
# Python
# BeautifulSoup
# Scraping
# HTML






# === Code Concepts Used ===
# requests.get(url)                  -> Sends an HTTP request to the given URL and retrieves the response

# BeautifulSoup(html, "html.parser") -> Parses the received HTML into a navigable structure

# soup.find() and soup.find_all()    -> Finds specific tags or all tags of a certain type in the HTML

# .text                              -> Extracts only the textual content from an HTML tag

# .write()                           -> Writes (saves) data to a file on the local system
