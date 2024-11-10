import requests
from bs4 import BeautifulSoup

# Function to scrape emoji names and codes from Unicode emoji list
def scrape_emoji_data():
    url = 'https://www.unicode.org/emoji/charts/emoji-list.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    emoji_map = {}
    
    # Find all table rows in the emoji list
    rows = soup.find_all('tr')
    
    for row in rows:
        columns = row.find_all('td')
        
        if len(columns) >= 3:  # Check if there are at least 3 columns (Unicode, emoji, name)
            emoji_code = columns[0].get_text(strip=True)
            emoji_char = columns[1].get_text(strip=True)
            emoji_name = columns[2].get_text(strip=True).lower().replace(' ', '_')

            # Add emoji and name to map
            if emoji_code and emoji_char:
                emoji_map[emoji_char] = emoji_name

    return emoji_map

# Scrape and print emoji map
emoji_map = scrape_emoji_data()
print(emoji_map)