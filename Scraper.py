
import requests
from bs4 import BeautifulSoup

def scrape_news():
    url = "https://www.bbc.com/news"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch page"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Example: grab headlines
    headlines = []
    for item in soup.select("h3"):
        title = item.get_text(strip=True)
        if title:
            headlines.append(title)
    
    return {"headlines": headlines}

