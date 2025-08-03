# News Web Scraping (extract titles)

import requests
##from bs4 import BeautifulSoup #  (commented code to avoid errors)

# Request the news page
url = "https://www.bbc.com/news"
response = requests.get(url)
##soup = BeautifulSoup(response.text, "html.parser") #  (commented code to avoid errors)

# Find headlines (example with <h3> tags)
##headlines = soup.find_all("h3")                    # Get all h3 tags #  (commented code to avoid errors)

# Save headlines to a file
#with open("headlines.txt", "w", encoding="utf-8") as file:  #  (commented code to avoid errors)
    ##for i, headline in enumerate(headlines[:5]):  # Limit to first 5 headlines  #  (commented code to avoid errors)
        ##text = headline.get_text(strip=True)       # Extract text cleanly  #  (commented code to avoid errors)
        ##print(f"{i+1}. {text}")                     # Print headline  #  (commented code to avoid errors)
        ##file.write(text + "\n")                      # Save to file  #  (commented code to avoid errors)

# Output (example):
#1. Global markets rally on economic recovery hopes
#2. Climate change report warns of extreme risks
#3. New tech innovations in renewable energy
#4. Sports update: local team wins championship
#5. Health officials discuss vaccine rollout






# Note: The above code is commented out to avoid errors since BeautifulSoup is not installed in this environment.
# If you want to run this code, make sure to install BeautifulSoup with:
# pip install beautifulsoup4
# and uncomment the relevant lines.



#Note:
#I need to test the code later. I'll come back in the future and redo the code with everything installed correctly.