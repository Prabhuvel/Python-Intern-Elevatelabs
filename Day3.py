import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Web_scraping" 
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all h2 tags
h2_tags = soup.find_all('h2')

# Open file in write mode to write the context in the .txt file
with open("h2_headings.txt", "w", encoding='utf-8') as file:
    for tag in h2_tags:
        heading = tag.text.strip()
        file.write(heading + "\n")
