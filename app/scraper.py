import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title else "No title"

    meta = soup.find("meta", attrs={"name": "description"})
    meta_description = meta["content"] if meta and meta.get("content") else "No meta description"

    headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])]

    img = soup.find("img")
    image = img["src"] if img and img.get("src") else None

    return {
        "title": title,
        "meta_description": meta_description,
        "headings": headings,
        "image": image
    }