# web_scraper.py

import requests
from bs4 import BeautifulSoup
import json
import os
import uuid


def scrape_website(url: str):
    """
    Scrapes structured paragraph data from a website.
    Returns list of structured article dictionaries.
    """

    print(f"Scraping website: {url}")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove unwanted tags
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()

    paragraphs = soup.find_all("p")

    articles = []
    seen_texts = set()

    for para in paragraphs:
        text = para.get_text().strip()

        if text and len(text) > 50 and text not in seen_texts:
            seen_texts.add(text)

            articles.append({
                "id": str(uuid.uuid4()),
                "source": url,
                "content": text,
                "length": len(text)
            })

    print(f"Total structured paragraphs scraped: {len(articles)}")
    return articles


def save_to_json(data, filename="data/raw_data.json"):
    os.makedirs("data", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"Data saved to {filename}")
